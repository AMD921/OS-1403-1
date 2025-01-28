# Dining Philosophers Problem Simulation

This is a Python simulation of the classic **Dining Philosophers Problem**, which demonstrates synchronization and deadlock avoidance in a multi-threaded environment. It uses threading, semaphores, and locks to manage philosophers who think and eat in a loop, with the goal of ensuring that no philosopher gets stuck waiting for forever (deadlock).

## How It Works

- **Philosophers** are represented as threads.
- Each philosopher has two forks, one to their left and one to their right.
- Philosophers alternate between **thinking** and **eating**.
- Only one philosopher can eat at a time, and they need both forks (left and right) to do so.
- The simulation prevents **deadlock** by limiting the number of concurrent diners and ensuring the longest-waiting philosopher gets a chance to eat.

## Key Components

- **Forks**: Represented by semaphores, each fork can only be held by one philosopher at a time.
- **Max Diners**: A semaphore to limit the number of philosophers eating at the same time (4 out of 5 in this case) to avoid deadlock.
- **Waiting Queue**: A deque tracks the order of philosophers waiting to eat.
- **Hunger Times**: Tracks the time each philosopher has been hungry to help prioritize who gets to eat first.

## Code Explanation

1. **Philosophers** are simulated using threads, where each thread represents a philosopher.
2. Each philosopher:
   - Thinks for a random time.
   - Becomes hungry and joins the waiting queue.
   - Waits for the longest-waiting philosopher to eat first (using the deque).
   - Acquires two forks (semaphores).
   - Eats for a random time.
   - Releases the forks and goes back to thinking.
3. **Logging** is used to trace the actions of each philosopher.
4. **Synchronization** is done using semaphores and locks to avoid deadlock and race conditions.

## Key Synchronization Techniques

- **Semaphores**: Used to control access to shared resources (forks) and limit the number of concurrent diners.
- **Lock**: Used to ensure that print statements are not interrupted by other threads, maintaining readable output.
- **Deque**: Used to track philosophers waiting to eat, ensuring that the longest-waiting philosopher gets the forks first.

## Usage

This simulation runs indefinitely, with philosophers continuously thinking and eating. You can stop it by interrupting the execution.

### Example Output

