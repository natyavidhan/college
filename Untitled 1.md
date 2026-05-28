# Home Server Documentation

Source conversation: fileciteturn0file0

---

# Overview

This document is a consolidated technical summary of the home server architecture, services, networking stack, storage strategy, media workflow, and utility infrastructure discussed throughout the development process of the server.

The goal of this document is to:

- Act as long-term documentation for the server
    
- Serve as a reference for future upgrades and maintenance
    
- Provide a clean foundation for writing blog posts or publishing the setup online
    
- Document both the practical implementation and the reasoning behind architectural decisions
    

This homelab is primarily designed around:

- Self-hosting
    
- Media streaming
    
- Remote access
    
- Document management
    
- Network-accessible utilities
    
- Personal cloud infrastructure
    
- Mobile-first usability
    
- Minimal dependence on commercial cloud services
    

The setup emphasizes:

- Simplicity
    
- Reliability
    
- Low maintenance
    
- Remote accessibility
    
- Docker-based deployment
    
- Tailscale networking
    
- Practical everyday usability over enterprise complexity
    

---

# Core Philosophy

The server architecture evolved around a few major goals:

## 1. Self-Hosted Personal Infrastructure

The server is intended to replace multiple cloud services with self-hosted alternatives.

Examples include:

- Personal cloud storage
    
- Music streaming
    
- Photo management
    
- Remote access
    
- Document archival
    
- Scanning workflows
    
- Local network services
    

## 2. Remote Accessibility Without Port Forwarding

One of the most important architectural decisions was avoiding:

- Router configuration complexity
    
- Public port exposure
    
- Dynamic DNS setups
    
- Traditional VPN management
    

Instead, the setup heavily relies on:

- Tailscale
    
- MagicDNS
    
- Internal reverse proxy routing
    

This creates a globally accessible private network while maintaining simplicity.

## 3. Media-Centric Usage

The server is heavily oriented around media workflows:

- FLAC music libraries
    
- Mobile streaming
    
- Smart transcoding
    
- SD-card caching
    
- Photo hosting
    
- Remote media access
    

The architecture prioritizes preserving archival-quality originals while still supporting low-bandwidth mobile usage.

## 4. Docker-First Infrastructure

Services are intended to run in containers wherever possible.

Benefits:

- Isolation
    
- Easier updates
    
- Simplified backups
    
- Portability
    
- Faster recovery
    
- Cleaner dependency management
    

---

# Network Architecture

## Core Stack

The final recommended architecture became:

```text
Tailscale
+ MagicDNS
+ Caddy
+ Docker services
```

This stack forms the backbone of the homelab.

---

## Tailscale

Tailscale acts as the secure networking layer.

Purpose:

- Remote access to all services
    
- Secure mesh VPN networking
    
- Cross-device connectivity
    
- Elimination of public port forwarding
    
- Simplified networking across devices
    

Devices connected through Tailscale include:

- Main server node
    
- Laptop
    
- Android phone
    
- Other future nodes
    

### Advantages

- NAT traversal handled automatically
    
- Encrypted connections
    
- Easy onboarding of new devices
    
- Works across mobile networks
    
- No public IP requirements
    
- Stable remote access
    

---

## MagicDNS

MagicDNS is used for internal hostname resolution.

Instead of relying on:

- Static IP addresses
    
- Local DNS hacks
    
- `/etc/hosts`
    
- AdGuard rewrites
    

Services become reachable through stable internal hostnames.

Example structure:

```text
main.tailnet-name.ts.net
agent.tailnet-name.ts.net
```

Potential internal service routing:

```text
immich.main.ts.net
nextcloud.main.ts.net
music.main.ts.net
```

### Benefits

- Human-readable endpoints
    
- Easier reverse proxy configuration
    
- Stable access from Android and laptops
    
- Cleaner service discovery
    

---

## Reverse Proxy Layer (Caddy)

Caddy is intended to act as the reverse proxy layer.

Responsibilities:

- Service routing
    
- HTTPS handling
    
- Internal domain mapping
    
- Reverse proxying to Docker containers
    

Example routing:

```caddy
photos.home {
    reverse_proxy agent:2283
}
```

Or using Tailscale hostnames:

```caddy
photos.home {
    reverse_proxy agent.tailnet-name.ts.net:2283
}
```

### Why Caddy?

Chosen because of:

- Extremely simple configuration
    
- Automatic HTTPS
    
- Lightweight deployment
    
- Docker friendliness
    
- Good compatibility with Tailscale
    

---

# Service Architecture

The server appears to follow a service-per-container approach.

Likely directory structure:

```text
~/services/
    immich/
    navidrome/
    scanservjs/
    nextcloud/
```

Each service contains:

- Docker Compose configuration
    
- Persistent data volumes
    
- Service-specific configs
    

---

# Media Infrastructure

## Music Stack

The music workflow is one of the most refined parts of the system.

### Components

- FLAC music archive
    
- Navidrome
    
- Symfonium
    
- On-the-fly transcoding
    
- SD-card smart caching
    

---

## FLAC Master Archive

The primary music library is stored in FLAC format.

Reasoning:

- Archival quality
    
- Lossless preservation
    
- Future-proofing
    
- Better metadata retention
    

Typical FLAC file sizes discussed:

```text
40–50 MB per song
```

This created challenges for mobile streaming over limited data plans.

---

## Navidrome

Navidrome is used as the self-hosted music streaming backend.

Responsibilities:

- Music indexing
    
- Library management
    
- Streaming
    
- User authentication
    
- API access for mobile apps
    
- On-the-fly transcoding
    

### Transcoding Workflow

Instead of streaming raw FLAC files to mobile devices:

```text
Phone
↓
Requests compressed stream
↓
Navidrome transcodes FLAC
↓
Streams Opus/AAC
```

This massively reduces bandwidth usage.

---

## Transcoding Strategy

Recommended codecs:

### Preferred

```text
Opus @ 96kbps
```

### Alternative

```text
AAC @ 128kbps
```

Benefits:

- Lower mobile data usage
    
- Better battery efficiency
    
- Smaller cache sizes
    
- Good perceptual quality on mobile
    

---

## ffmpeg Integration

Navidrome requires ffmpeg for transcoding.

Validation command:

```bash
docker exec -it navidrome ffmpeg -version
```

Suggested configuration:

```yaml
environment:
  ND_TRANSCODINGCACHESIZE: 2GB
  ND_IMAGECACHESIZE: 500MB
```

---

## Symfonium Configuration

Symfonium is used as the mobile client.

Features utilized:

- Smart transcoding
    
- SD card caching
    
- Offline playback
    
- Network-aware quality switching
    

### Network Rules

Desired behavior:

```text
WiFi → Original FLAC
Mobile Data → Transcoded Audio
```

### Offline Cache

The setup leverages:

- Smart caching
    
- SD card storage
    
- Cached streamed tracks
    
- Offline downloads
    

This minimizes repeated mobile data usage.

---

## Expected Data Savings

### Raw FLAC

```text
~40 MB/song
25 songs ≈ 1 GB
```

### Opus 96kbps

```text
~2.5 MB/song
300–400 songs ≈ 1 GB
```

This optimization fundamentally changes the practicality of remote streaming.

---

# Photo and Cloud Services

## Immich

Immich is referenced as part of the hosted stack.

Purpose:

- Self-hosted photo backup
    
- Mobile gallery synchronization
    
- Photo organization
    
- Remote access to media
    

Likely accessible through:

```text
immich.main.ts.net
```

---

## Nextcloud

Nextcloud is also referenced as part of the service architecture.

Purpose:

- Personal cloud storage
    
- File synchronization
    
- Cross-device access
    
- Document management
    

Potential uses:

- Notes
    
- File backups
    
- College materials
    
- Shared storage
    
- Mobile sync
    

---

# Scanner and Document Workflow

One particularly interesting part of the setup is converting a USB printer/scanner into a network-accessible scanning appliance.

Hardware referenced:

```text
HP Ink Tank 310
```

---

## Scanner Stack

Base packages:

```bash
sudo apt install sane-utils simple-scan -y
```

Detection:

```bash
scanimage -L
```

Optional HP support:

```bash
sudo apt install hplip -y
hp-plugin
```

---

## scanservjs

The preferred scanning frontend is:

```text
scanservjs
```

Reasoning:

- Browser-accessible scanning
    
- Phone compatibility
    
- Multi-page PDF support
    
- Remote usability through Tailscale
    
- Simple deployment
    

### Docker Compose

```yaml
services:
  scanservjs:
    image: sbs20/scanservjs:latest
    container_name: scanservjs
    ports:
      - "8084:8080"
    devices:
      - /dev/bus/usb:/dev/bus/usb
    volumes:
      - ./data:/var/lib/scanservjs
    restart: unless-stopped
```

### Access Pattern

```text
http://192.168.1.110:8084
```

or eventually:

```text
http://scan.home
```

---

## Paperless-ngx Integration

A more advanced future architecture includes:

```text
Printer
↓
USB connection
↓
Main Node
↓
scanservjs
↓
Paperless-ngx
↓
OCR + searchable archive
```

This transforms the homelab into a document archival system.

### Use Cases

- Bills
    
- IDs
    
- Receipts
    
- Contracts
    
- Tax documents
    
- Medical documents
    
- College paperwork
    
- Handwritten notes
    

### Benefits

- OCR indexing
    
- Searchable PDFs
    
- Tagging
    
- Categorization
    
- Long-term storage
    
- Centralized document management
    

---

# Remote Access Strategy

One of the strongest design decisions in the setup is the avoidance of public exposure.

The architecture intentionally avoids:

- Public ports
    
- Complex firewall rules
    
- Traditional VPS tunnels
    
- Router-level port forwarding
    

Instead:

```text
Device
↓
Tailscale Tailnet
↓
MagicDNS
↓
Reverse Proxy
↓
Docker Service
```

This dramatically reduces complexity while still allowing:

- Global access
    
- Mobile usability
    
- Secure connectivity
    
- Stable service discovery
    

---

# Mobile-Centric Design

A large portion of the infrastructure decisions revolve around Android usability.

The setup prioritizes:

- Remote accessibility
    
- Low mobile data usage
    
- SD card integration
    
- Browser-accessible tools
    
- Network-aware streaming
    

This makes the homelab usable beyond the local network.

---

# Storage Philosophy

Although exact hardware storage details were not included in the conversation, the storage strategy can still be inferred.

## Likely Characteristics

- Large-capacity media storage
    
- Persistent Docker volumes
    
- Centralized media archive
    
- Long-term FLAC storage
    
- Mixed utility + archival usage
    

## Workload Types

- Music libraries
    
- Photos
    
- Documents
    
- OCR archives
    
- Docker persistent data
    
- App configurations
    

---

# Operational Design Principles

## Simplicity Over Enterprise Complexity

The infrastructure intentionally avoids overengineering.

Examples:

- Tailscale instead of complex VPNs
    
- Caddy instead of heavier reverse proxy stacks
    
- Docker Compose instead of Kubernetes
    
- MagicDNS instead of self-managed DNS servers
    

This improves:

- Maintainability
    
- Reliability
    
- Ease of debugging
    
- Upgrade simplicity
    

---

## Self-Hosting Priorities

The overall server direction strongly emphasizes:

- Ownership of data
    
- Independence from subscriptions
    
- Long-term archival
    
- Local-first infrastructure
    
- Cross-device synchronization
    

---

# Current Service Summary

## Networking

- Tailscale
    
- MagicDNS
    
- Caddy
    

## Media

- Navidrome
    
- Symfonium
    
- FLAC archive
    
- ffmpeg transcoding
    

## Cloud

- Nextcloud
    
- Immich
    

## Document Infrastructure

- scanservjs
    
- Paperless-ngx (planned/integrated architecture)
    
- SANE
    
- HPLIP
    

## Containerization

- Docker
    
- Docker Compose
    

---

# Future Expansion Possibilities

Based on the architectural direction, future additions could naturally include:

## Infrastructure

- Automated backups
    
- Monitoring dashboards
    
- UPS integration
    
- RAID or ZFS
    
- Snapshotting
    

## Media

- Jellyfin
    
- Audiobookshelf
    
- Lidarr
    
- Automated transcoding pipelines
    

## Productivity

- Gitea
    
- Syncthing
    
- Obsidian sync
    
- Self-hosted note systems
    

## Networking

- Tailscale Funnel
    
- HTTPS public endpoints
    
- Zero-trust service access
    

---

# Strengths of the Architecture

## 1. Practicality

The setup solves real daily problems instead of existing purely as a technical experiment.

## 2. Remote Accessibility

The system works from:

- Home WiFi
    
- Mobile networks
    
- Android devices
    
- Laptops
    

without requiring complicated networking.

## 3. Efficient Media Workflow

The FLAC + transcoding architecture preserves quality while minimizing mobile bandwidth.

## 4. Expandability

The Docker-based structure allows gradual scaling.

## 5. Low Operational Overhead

The stack is relatively lightweight and maintainable.

---

# Potential Weaknesses / Areas To Improve

## 1. Backups

No backup strategy was explicitly documented.

Critical next step:

- Automated backups
    
- Offsite copies
    
- Snapshot schedules
    

## 2. Monitoring

No observability stack was mentioned.

Potential additions:

- Grafana
    
- Prometheus
    
- Uptime Kuma
    

## 3. Storage Redundancy

No RAID or redundancy architecture was discussed.

Future improvements could include:

- RAID1/RAID5
    
- ZFS
    
- Scheduled integrity checks
    

## 4. Secret Management

Credentials and environment handling were not documented.

Future improvements:

- `.env` files
    
- Secret management
    
- Vault systems
    

---

# Final Architecture Snapshot

```text
                           Internet
                               ↓
                        Tailscale Mesh
                               ↓
                     MagicDNS Resolution
                               ↓
                           Caddy
                               ↓
        ┌──────────────────────────────────────┐
        │                                      │
        │         Docker Host Server           │
        │                                      │
        ├──────────────────────────────────────┤
        │ Navidrome                            │
        │ Immich                               │
        │ Nextcloud                            │
        │ scanservjs                           │
        │ Paperless-ngx                        │
        │ Other future services                │
        └──────────────────────────────────────┘
                               ↓
                  Media + Documents + Storage
```

---

# Conclusion

This homelab evolved into a practical personal infrastructure platform rather than just a hobby server.

The architecture focuses on:

- Real-world usability
    
- Remote accessibility
    
- Media preservation
    
- Self-hosting convenience
    
- Low-maintenance networking
    
- Mobile-first workflows
    

The most notable strengths are:

- Tailscale-centric networking
    
- Smart media transcoding
    
- Browser-based utility access
    
- Dockerized modular services
    
- Expandable architecture
    

Overall, the setup represents a strong modern self-hosted stack that balances usability, scalability, and simplicity without drifting into unnecessary complexity.