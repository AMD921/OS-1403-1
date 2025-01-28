# Dining Philosophers Problem Simulation

## Description
This project is a simple simulation of the classic **Dining Philosophers Problem** in computer science, which illustrates challenges in concurrent programming, particularly regarding resource sharing and synchronization.

The simulation involves five philosophers sitting at a round table. Each philosopher alternates between thinking and eating, but to eat, they require two forks (shared resources) on their left and right. Proper synchronization ensures that no two philosophers use the same fork simultaneously and helps avoid issues like deadlock.

## How It Works
- Philosophers are represented as threads.
- Semaphores are used to control access to forks.
- A lock (`print_lock`) ensures clean, synchronized output.
- Randomized thread order simulates unpredictable execution.

## Features
- Proper thread synchronization using semaphores.
- Print statements using f-strings for better readability.
- Deadlock-prone simple implementation, useful for educational purposes.

## Requirements
- Python 3.x

## Usage
1. Clone the repository or copy the code.
2. Run the script using:
   ```bash
   python dining_philosophers.py
   ```
3. Observe the philosophers thinking, eating, and releasing forks.

## Example Output
```text
Philosopher 0 is thinking
Philosopher 2 is thinking
Philosopher 0 is Hungry
Philosopher 0 is eating
Philosopher 3 is Hungry
Philosopher 4 is thinking
Philosopher 0 is finished eating and now thinking
Philosopher 4 is Hungry
```

