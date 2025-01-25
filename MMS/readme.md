# Memory Management Simulator

This project implements a simple memory management simulation using various memory allocation and page replacement algorithms. It allows you to allocate memory for processes, simulate page access, and handle page faults with specified algorithms.

---

## Features

1. **Memory Allocation Algorithms**:
   - First Fit
   - Best Fit
   - Worst Fit

2. **Page Replacement Algorithms**:
   - FIFO (First In First Out)
   - LRU (Least Recently Used)

3. **Simulation**:
   - Allocate memory for processes.
   - Simulate page accesses and handle page faults.
   - Track total page faults during the simulation.

---

## How to Use

### 1. Prerequisites
- Python 3.x is required to run the simulation.

### 2. Running the Simulation
- Clone or download the repository.
- Run the `main()` function in the script to execute the memory management simulation.

### 3. Key Classes and Methods
#### **`Process`**
- Represents a process with the following attributes:
  - `pid`: Process ID.
  - `size`: Total memory size required by the process.
  - `pages`: List of allocated pages.

#### **`MemoryManager`**
- Manages memory allocation and page replacement.
  - `allocate_memory(process)`: Allocates memory for a given process.
  - `access_page(process, page_number)`: Simulates a page access.
  - **Allocation Algorithms**:
    - `first_fit(process, num_pages_required)`
    - `best_fit(process, num_pages_required)`
    - `worst_fit(process, num_pages_required)`
  - **Replacement Algorithms**:
    - `fifo_replace(page_id)`
    - `lru_replace(page_id)`

---

## Example Simulation

The `main()` function demonstrates:
1. Setting up the memory manager with specified memory size, page size, allocation algorithm, and replacement algorithm.
2. Creating example processes and allocating memory.
3. Simulating page accesses and handling page faults.

```python
memory_size = 100
page_size = 10
allocation_algorithm = "First Fit"
replacement_algorithm = "LRU"

memory_manager = MemoryManager(memory_size, page_size, allocation_algorithm, replacement_algorithm)

# Example processes
processes = [
    Process("A", 40),
    Process("B", 30),
    Process("C", 50)
]

# Allocating memory for processes
for process in processes:
    memory_manager.allocate_memory(process)

# Simulating page access
page_access_sequence = [
    ("A", 1), ("B", 1), ("A", 2), ("C", 1),
    ("A", 3), ("C", 2), ("B", 2), ("C", 3),
    ("A", 4), ("C", 4), ("B", 3), ("C", 5)
]

for process_id, page_number in page_access_sequence:
    process = next((p for p in processes if p.pid == process_id), None)
    if process:
        memory_manager.access_page(process, page_number)

print(f"Total Page Faults: {memory_manager.page_faults}")
