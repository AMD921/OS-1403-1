from threading import Thread, Semaphore, Lock
import time
import random

# Semaphores and lock for synchronizing print statements
no_philo = 5
forks = [Semaphore(1) for i in range(no_philo)]
status = ["thinking" for i in range(no_philo)]
print_lock = Lock()

def philosopher(i):
    with print_lock:  # Ensures that only one philosopher prints at a time
        print(f"Philosopher {i} is {status[i]}")
    
    time.sleep(0.3)
    
    with print_lock:
        print(f"Philosopher {i} is Hungry")
    
    forks[i].acquire()
    forks[(i+1)%no_philo].acquire()

    with print_lock:
        print(f"Philosopher {i} is eating")
    
    time.sleep(1)
    
    with print_lock:
        print(f"Philosopher {i} is finished eating and now thinking")
    
    forks[i].release()
    forks[(i+1)%no_philo].release()

# Create threads for philosophers
total = [Thread(target=philosopher, args=[i]) for i in range(no_philo)]
random.shuffle(total)

# Start all threads
for i in total:
    i.start()

# Wait for all threads to finish
for i in total:
    i.join()
