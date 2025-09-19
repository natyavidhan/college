processes = []

n = int(input("Enter Number of Processes: "))
for i in range(n):
    data = input(f"Enter AT and BT (space separated): ")
    at, bt = map(int, data.split())
    processes.append({"pid": i + 1, "arrival_time": at, "burst_time": bt})
    
queue = []
time = 0
completed = 0
gantt_chart = []
remaining_processes = processes.copy()
current_process = None
start_time = 0

while completed < n:
    for process in list(remaining_processes):
        if process["arrival_time"] <= time:
            queue.append(process)
            remaining_processes.remove(process)
    
    if current_process is None and queue:
        current_process = queue.pop(0)
        start_time = time
        current_process["remaining_time"] = current_process["burst_time"]
    
    if current_process:
        current_process["remaining_time"] -= 1
        
        if current_process["remaining_time"] == 0:
            end_time = time + 1
            gantt_chart.append((current_process["pid"], start_time, end_time))
            current_process = None
            completed += 1
    
    time += 1
        
print("\nGantt Chart:")
for pid, start, end in gantt_chart:
    print(f"| P{pid} ({start} - {end}) ", end="")
print("|")

process_stats = {}
for pid, start, end in gantt_chart:
    process_stats[pid] = {"completion_time": end}

for process in processes:
    pid = process["pid"]
    at = process["arrival_time"]
    bt = process["burst_time"]
    ct = process_stats[pid]["completion_time"]
    
    tat = ct - at
    wt = tat - bt
    
    process_stats[pid].update({
        "arrival_time": at,
        "burst_time": bt,
        "turn_around_time": tat,
        "waiting_time": wt
    })

print("\nProcess Stats:")
print("PID\tAT\tBT\tCT\tTAT\tWT")
total_tat = 0
total_wt = 0
for pid in sorted(process_stats.keys()):
    stat = process_stats[pid]
    at = stat["arrival_time"]
    bt = stat["burst_time"]
    ct = stat["completion_time"]
    tat = stat["turn_around_time"]
    wt = stat["waiting_time"]
    total_tat += tat
    total_wt += wt
    print(f"P{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

print(f"\nAverage Turn Around Time: {total_tat/n:.2f}")
print(f"Average Waiting Time: {total_wt/n:.2f}")