import os
import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=None):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.response_time = None

def fcfs(processes, context_switch_time):
    processes.sort(key=lambda x: x.arrival_time)
    current_time = 0
    gantt_chart = []

    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        gantt_chart.append((process.pid, current_time, current_time + process.burst_time))
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        process.response_time = current_time - process.arrival_time

        current_time += process.burst_time + context_switch_time

    return gantt_chart

def sjf(processes, context_switch_time):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0
    gantt_chart = []
    completed = 0
    n = len(processes)
    
    while completed < n:
        available = [p for p in processes if p.arrival_time <= current_time and p.completion_time == 0]
        if not available:
            current_time += 1
            continue

        process = min(available, key=lambda x: x.burst_time)
        gantt_chart.append((process.pid, current_time, current_time + process.burst_time))
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        process.response_time = current_time - process.arrival_time

        current_time += process.burst_time + context_switch_time
        completed += 1

    return gantt_chart

def round_robin(processes, time_quantum, context_switch_time):
    current_time = 0
    gantt_chart = []
    queue = [p for p in sorted(processes, key=lambda x: x.arrival_time)]

    while queue:
        process = queue.pop(0)

        if process.remaining_time > time_quantum:
            gantt_chart.append((process.pid, current_time, current_time + time_quantum))
            process.remaining_time -= time_quantum
            current_time += time_quantum + context_switch_time
            queue.extend([p for p in processes if p.arrival_time <= current_time and p not in queue and p.remaining_time > 0])
            queue.append(process)
        else:
            gantt_chart.append((process.pid, current_time, current_time + process.remaining_time))
            current_time += process.remaining_time + context_switch_time
            process.completion_time = current_time - context_switch_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            process.response_time = process.response_time or (current_time - process.burst_time - process.arrival_time)
            process.remaining_time = 0

    return gantt_chart

def priority_scheduling(processes, context_switch_time):
    processes.sort(key=lambda x: (x.arrival_time, x.priority))
    current_time = 0
    gantt_chart = []
    completed = 0
    n = len(processes)

    while completed < n:
        available = [p for p in processes if p.arrival_time <= current_time and p.completion_time == 0]
        if not available:
            current_time += 1
            continue

        process = min(available, key=lambda x: x.priority)
        gantt_chart.append((process.pid, current_time, current_time + process.burst_time))
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        process.response_time = current_time - process.arrival_time

        current_time += process.burst_time + context_switch_time
        completed += 1

    return gantt_chart

def print_metrics(processes):
    print("\nProcess Metrics:")
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting\tResponse")
    for p in processes:
        print(f"{p.pid}\t{p.arrival_time}\t{p.burst_time}\t{p.completion_time}\t\t{p.turnaround_time}\t\t{p.waiting_time}\t\t{p.response_time}")

def plot_gantt_chart(gantt_chart):
    fig, gnt = plt.subplots()
    gnt.set_ylim(0, 50)
    gnt.set_xlim(0, max(end for _, _, end in gantt_chart))

    gnt.set_xlabel('Time')
    gnt.set_ylabel('Processes')
    gnt.set_yticks([15])
    gnt.set_yticklabels(['Processes'])
    gnt.grid(True)

    for pid, start, end in gantt_chart:
        gnt.broken_barh([(start, end - start)], (10, 10), facecolors=('tab:blue'))

    plt.show()

def main():
    processes = [
        Process(1, 0, 8),
        Process(2, 1, 4),
        Process(3, 2, 9),
        Process(4, 3, 5)
    ]

    context_switch_time = 1
    print("Choose Scheduling Algorithm:")
    print("1. FCFS")
    print("2. SJF")
    print("3. Round Robin")
    print("4. Priority Scheduling")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        gantt_chart = fcfs(processes, context_switch_time)
    elif choice == 2:
        gantt_chart = sjf(processes, context_switch_time)
    elif choice == 3:
        time_quantum = int(input("Enter Time Quantum: "))
        gantt_chart = round_robin(processes, time_quantum, context_switch_time)
    elif choice == 4:
        for p in processes:
            p.priority = int(input(f"Enter priority for Process {p.pid}: "))
        gantt_chart = priority_scheduling(processes, context_switch_time)
    else:
        print("Invalid choice!")
        return

    print_metrics(processes)
    plot_gantt_chart(gantt_chart)

if __name__ == "__main__":
    main()
