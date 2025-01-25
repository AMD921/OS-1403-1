class Process:
    def __init__(self, pid, size):
        self.pid = pid
        self.size = size
        self.pages = []  # Pages allocated to this process


class MemoryManager:
    def __init__(self, total_memory_size, page_size, allocation_algorithm, replacement_algorithm):
        self.total_memory_size = total_memory_size
        self.page_size = page_size
        self.num_pages = total_memory_size // page_size
        self.free_memory = self.num_pages
        self.allocation_algorithm = allocation_algorithm
        self.replacement_algorithm = replacement_algorithm
        self.memory = [None] * self.num_pages  # Simulates memory with page slots
        self.page_table = {}  # Tracks pages allocated to processes
        self.page_faults = 0
        self.access_order = []  # Tracks page access for replacement algorithms

    def allocate_memory(self, process):
        num_pages_required = -(-process.size // self.page_size)  # Ceiling division
        if num_pages_required > self.free_memory:
            print(f"Insufficient memory for Process {process.pid}.")
            return False

        if self.allocation_algorithm == "First Fit":
            allocated = self.first_fit(process, num_pages_required)
        elif self.allocation_algorithm == "Best Fit":
            allocated = self.best_fit(process, num_pages_required)
        elif self.allocation_algorithm == "Worst Fit":
            allocated = self.worst_fit(process, num_pages_required)
        else:
            raise ValueError("Unknown memory allocation algorithm.")
        return allocated

    def first_fit(self, process, num_pages_required):
        contiguous_count = 0
        start_index = -1

        for i in range(self.num_pages):
            if self.memory[i] is None:
                if start_index == -1:
                    start_index = i
                contiguous_count += 1
                if contiguous_count == num_pages_required:
                    break
            else:
                contiguous_count = 0
                start_index = -1

        if contiguous_count == num_pages_required:
            for i in range(start_index, start_index + num_pages_required):
                self.memory[i] = process.pid
            process.pages.extend(range(start_index, start_index + num_pages_required))
            self.free_memory -= num_pages_required
            return True

        print(f"First Fit: Failed to allocate memory for Process {process.pid}.")
        return False

    def best_fit(self, process, num_pages_required):
        gaps = []
        current_gap_size = 0
        current_gap_start = -1

        for i in range(self.num_pages):
            if self.memory[i] is None:
                if current_gap_start == -1:
                    current_gap_start = i
                current_gap_size += 1
            else:
                if current_gap_size > 0:
                    gaps.append((current_gap_start, current_gap_size))
                current_gap_start = -1
                current_gap_size = 0

        if current_gap_size > 0:
            gaps.append((current_gap_start, current_gap_size))

        gaps = [gap for gap in gaps if gap[1] >= num_pages_required]
        if not gaps:
            print(f"Best Fit: No suitable gap for Process {process.pid}.")
            return False

        best_gap = min(gaps, key=lambda x: x[1])
        for i in range(best_gap[0], best_gap[0] + num_pages_required):
            self.memory[i] = process.pid
        process.pages.extend(range(best_gap[0], best_gap[0] + num_pages_required))
        self.free_memory -= num_pages_required
        return True

    def worst_fit(self, process, num_pages_required):
        gaps = []
        current_gap_size = 0
        current_gap_start = -1

        for i in range(self.num_pages):
            if self.memory[i] is None:
                if current_gap_start == -1:
                    current_gap_start = i
                current_gap_size += 1
            else:
                if current_gap_size > 0:
                    gaps.append((current_gap_start, current_gap_size))
                current_gap_start = -1
                current_gap_size = 0

        if current_gap_size > 0:
            gaps.append((current_gap_start, current_gap_size))

        gaps = [gap for gap in gaps if gap[1] >= num_pages_required]
        if not gaps:
            print(f"Worst Fit: No suitable gap for Process {process.pid}.")
            return False

        worst_gap = max(gaps, key=lambda x: x[1])
        for i in range(worst_gap[0], worst_gap[0] + num_pages_required):
            self.memory[i] = process.pid
        process.pages.extend(range(worst_gap[0], worst_gap[0] + num_pages_required))
        self.free_memory -= num_pages_required
        return True

    def access_page(self, process, page_number):
        page_id = (process.pid, page_number)
        if page_id in self.page_table:
            print(f"Process {process.pid}, Page {page_number} already in memory.")
        else:
            if len(self.access_order) == self.num_pages:
                self.replace_page(page_id)
            else:
                self.load_page(page_id)
            self.page_faults += 1

    def load_page(self, page_id):
        self.access_order.append(page_id)
        self.page_table[page_id] = len(self.access_order) - 1
        print(f"Loaded Page {page_id} into memory.")

    def replace_page(self, page_id):
        if self.replacement_algorithm == "FIFO":
            self.fifo_replace(page_id)
        elif self.replacement_algorithm == "LRU":
            self.lru_replace(page_id)
        else:
            raise ValueError("Unknown page replacement algorithm.")

    def fifo_replace(self, page_id):
        evicted_page = self.access_order.pop(0)
        self.access_order.append(page_id)
        del self.page_table[evicted_page]
        self.page_table[page_id] = len(self.access_order) - 1
        print(f"Replaced Page {evicted_page} with {page_id} (FIFO).")

    def lru_replace(self, page_id):
        evicted_page = self.access_order.pop(0)
        self.access_order.append(page_id)
        del self.page_table[evicted_page]
        self.page_table[page_id] = len(self.access_order) - 1
        print(f"Replaced Page {evicted_page} with {page_id} (LRU).")


def main():
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

    for process in processes:
        memory_manager.allocate_memory(process)

    # Page Access Simulation
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


if __name__ == "__main__":
    main()
