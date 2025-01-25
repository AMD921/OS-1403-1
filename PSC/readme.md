# Process Scheduling Simulator

## Overview

This Python program simulates various process scheduling algorithms used in operating systems. The goal of the project is to help users understand how these algorithms work by providing a detailed simulation and visual representation of process execution.

## Features

- Simulates the following scheduling algorithms:
  1. **First Come First Serve (FCFS)**
  2. **Shortest Job First (SJF)**
  3. **Round Robin (RR)**
  4. **Priority Scheduling**
- Outputs process metrics such as:
  - Completion Time
  - Turnaround Time
  - Waiting Time
  - Response Time
- Visualizes the process execution order using a Gantt Chart.

## Requirements

- Python 3.x
- Matplotlib library (for Gantt chart visualization)

## Installation

1. Clone this repository or download the code.
2. Install the required library by running:
   ```bash
   pip install matplotlib
   ```

## Usage

1. Run the program:

   ```bash
   python PSC.py
   ```



1. Follow the prompts to:

   - Select a scheduling algorithm.
   - Provide required inputs (e.g., time quantum for Round Robin, priorities for Priority Scheduling).

2. View the calculated metrics and the Gantt Chart.

## Example Input

- Default processes used in the simulation:
  ```
  Process 1: Arrival Time = 0, Burst Time = 8
  Process 2: Arrival Time = 1, Burst Time = 4
  Process 3: Arrival Time = 2, Burst Time = 9
  Process 4: Arrival Time = 3, Burst Time = 5
  ```

## Output

- Metrics for each process:
  - Completion Time
  - Turnaround Time
  - Waiting Time
  - Response Time
- Gantt Chart showing the process execution timeline.

## Supported Scheduling Algorithms

### 1. **First Come First Serve (FCFS)**

- Processes are executed in the order they arrive.

### 2. **Shortest Job First (SJF)**

- The process with the shortest burst time is executed first.

### 3. **Round Robin (RR)**

- Each process is assigned a fixed time quantum and executed cyclically.

### 4. **Priority Scheduling**

- Processes are executed based on priority (lower value = higher priority).

## Notes

- Context switching time is configurable (default: 1 unit).
- Priorities and time quantum are user-defined during runtime.
