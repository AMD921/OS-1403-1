
# Memory Management Simulator

This Python program simulates memory allocation and page replacement algorithms for processes in a system. It allows for flexible configuration of memory size, page size, allocation algorithms, and page replacement strategies.

## Features

- **Memory Allocation Algorithms**:
  - **First Fit**
  - **Best Fit**
  - **Worst Fit**

- **Page Replacement Algorithms**:
  - **FIFO (First-In-First-Out)**
  - **LRU (Least Recently Used)**

- Tracks memory allocation, deallocation, and page faults.
- Simulates a sequence of page accesses for processes.

---

## How It Works

1. **Processes**: Each process has a unique ID and memory size (in bytes). The memory manager allocates memory based on the selected allocation algorithm.
2. **Pages**: Memory is divided into fixed-sized pages. Processes are allocated pages as per their memory requirements.
3. **Page Replacement**: When memory is full, the simulator uses the specified replacement algorithm to evict pages.

---

## Getting Started

### Prerequisites

- Python 3.x

### Running the Program

1. Clone the repository or download the script.
2. Run the script:
   ```bash
   python MMS.py
   ```

### Configuration

You can configure the following parameters in the `main()` function:
- **Memory Size**: Total memory size (e.g., 100 units).
- **Page Size**: Size of each page (e.g., 10 units).
- **Allocation Algorithm**: Choose from `First Fit`, `Best Fit`, or `Worst Fit`.
- **Replacement Algorithm**: Choose from `FIFO` or `LRU`.

---

## Example Output

1. Processes are allocated memory:
   ```
   Process A allocated memory using First Fit.
   Process B allocated memory using First Fit.
   Process C allocated memory using First Fit.
   ```

2. Page access simulation:
   ```
   Loaded Page ('A', 1) into memory.
   Loaded Page ('B', 1) into memory.
   Replaced Page ('A', 1) with ('C', 1) (LRU).
   ```

3. Total page faults:
   ```
   Total Page Faults: 6
   ```

---

## Customization

- Add or modify processes by editing the `processes` list in `main()`.
- Change the sequence of page accesses using the `page_access_sequence` list.

---
