import threading
import time
import random

# Number of philosophers
N = 5

# Semaphore for forks
forks = [threading.Semaphore(1) for _ in range(N)]

# Semaphore to prevent deadlock
room = threading.Semaphore(N - 1)

# States of philosophers
states = ["Thinking"] * N

# Lock for printing states
state_lock = threading.Lock()

# Timer for hunger duration
hunger_time = [0] * N

def print_states():
    """Print the current states of philosophers and their hunger times"""
    with state_lock:
        status = [f"Philosopher {i}: {states[i]} (Hunger Time: {hunger_time[i]:.2f}s)" for i in range(N)]
        print("\n".join(status))
        print("-" * 50)

def philosopher(philosopher_id):
    global hunger_time
    while True:
        # Thinking
        states[philosopher_id] = "Thinking"
        print_states()
        time.sleep(random.uniform(1, 3))

        # Getting hungry
        states[philosopher_id] = "Hungry"
        hunger_start = time.time()
        print_states()

        # Enter the room (prevent deadlock)
        room.acquire()

        # Acquire forks
        forks[philosopher_id].acquire()
        forks[(philosopher_id + 1) % N].acquire()

        # Eating
        hunger_time[philosopher_id] += time.time() - hunger_start
        states[philosopher_id] = "Eating"
        print_states()
        time.sleep(random.uniform(1, 2))

        # Release forks
        forks[philosopher_id].release()
        forks[(philosopher_id + 1) % N].release()

        # Exit the room
        room.release()

if __name__ == "__main__":
    threads = []
    for i in range(N):
        t = threading.Thread(target=philosopher, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
