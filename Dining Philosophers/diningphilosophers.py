import logging
from threading import Thread, Semaphore, Lock
import time
import random
from collections import deque

# Setup logging for traceability
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# Semaphores and lock for synchronizing print statements
no_philo = 5
forks = [Semaphore(1) for _ in range(no_philo)]
max_diners = Semaphore(no_philo - 1)  # Prevent deadlock by allowing only 4 philosophers to eat concurrently
status = ["thinking" for _ in range(no_philo)]
print_lock = Lock()
waiting_queue = deque()  # Queue to track philosophers waiting to eat
hunger_times = [0 for _ in range(no_philo)]  # Track hunger times

start_time = time.time()

def philosopher(i):
    global waiting_queue
    
    while True:  # Simulate continuous cycles of thinking and eating
        # Thinking phase
        logging.info(f"Philosopher {i} is thinking.")
        
        time.sleep(random.uniform(0.2, 0.5))
        
        # Hungry phase
        logging.info(f"Philosopher {i} is hungry.")
        hunger_times[i] = time.time() - start_time  # Update hunger duration
        
        waiting_queue.append(i)

        # Synchronize fork acquisition with priority to longest waiting philosopher
        max_diners.acquire()  # Limit concurrent dining philosophers

        while waiting_queue[0] != i:
            time.sleep(0.1)  # Busy wait until it's their turn

        forks[i].acquire()
        forks[(i + 1) % no_philo].acquire()

        waiting_queue.popleft()  # Remove philosopher from queue once they start eating

        # Eating phase
        logging.info(f"Philosopher {i} is eating.")
        
        time.sleep(random.uniform(0.8, 1.5))  # Eating time

        # Finished eating phase
        logging.info(f"Philosopher {i} is finished eating and now thinking.")

        forks[i].release()
        forks[(i + 1) % no_philo].release()

        max_diners.release()  # Allow another philosopher to enter dining state

        time.sleep(random.uniform(0.2, 0.5))

# Create threads for philosophers
total = [Thread(target=philosopher, args=[i]) for i in range(no_philo)]

# Start all threads
for thread in total:
    thread.start()

# Join threads (optional, in a real scenario this could run indefinitely)
for thread in total:
    thread.join()
