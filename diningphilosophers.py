from threading import Thread
from threading import Semaphore
import time

#Semaphores needed
philosophers = 5
forks = [Semaphore(1) for i in range(philosophers)]
status = ["thinking" for i in range(philosophers)]

def philosopher(i):
    print("Philosopher",i,"is",status[i])
    time.sleep(0.3)
    print("Philosopher",i,"is Hungry")
    forks[i].acquire()
    forks[(i+1)%philosophers].acquire()

    print("Philosopher",i,"is eating")
    time.sleep(1)
    
    print("Philosopher",i,"Is finished eating and now thinking")

    forks[i].release()
    forks[(i+1)%philosophers].release()

import random
total = [Thread(target=philosopher,args=[i]) for i in range(philosophers)]
random.shuffle(total)

for i in total:
    i.start()

for i in total:
    i.join()
