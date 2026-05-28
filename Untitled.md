Ollama, Bitwarden, uptimekuma, SearXNG, GitTea, immich, qBittorrent, local copy of wikipedia, soulseek, navidrome, jellyfin, a NAS, a S3 bucket, and all kinds of DBs (mongo, postgress and redis)

ai.home {
    reverse_proxy 192.168.1.110:3000
}

home.home {
    reverse_proxy 192.168.1.110:3001
}

uptime.home {
    reverse_proxy 192.168.1.110:3002
}

vault.home {
    reverse_proxy 192.168.1.110:3004
}

nextcloud.home {
    reverse_proxy 192.168.1.110:8081
}

traccar.home {
    reverse_proxy 192.168.1.110:8082
}

search.home {
    reverse_proxy 192.168.1.110:8088
}

portainer.home {
    reverse_proxy 192.168.1.110:9443 {
        transport http {
            tls_insecure_skip_verify
        }
    }
}


# =========================
# AGENT NODE (192.168.1.111)
# =========================

git.home {
    reverse_proxy 192.168.1.111:3000
}

photos.home {
    reverse_proxy 192.168.1.111:2283
}

torrent.home {
    reverse_proxy 192.168.1.111:8080
}

wiki.home {
    reverse_proxy 192.168.1.111:8083
}

soulseek.home {
    reverse_proxy 192.168.1.111:5030
}

music.home {
    reverse_proxy 192.168.1.111:4533
}

lidarr.home {
    reverse_proxy 192.168.1.111:8686
}

storage.home {
    reverse_proxy 192.168.1.111:9000
}

maloja.home {
    reverse_proxy 192.168.1.111:42010
}