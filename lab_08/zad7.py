from collections import Counter, deque
import random
import time
import numpy as np

def create_kolo_fortuny(*args):
    counter = Counter(args)
    return deque(counter.items())

def spinit(ticks: int):
    waits = np.logspace(0.0, 1.0, num=ticks) / ticks
    for tick in range(ticks):
        print(f'{tick}', end='')
        time.sleep(waits[tick])
        print('\r', end='')
        
kolo_fortuny = create_kolo_fortuny(5, 6, 6, 6, 2, 1, 3, 1 , 8, 2, 5, 1, 5)


for i in range(2):
    kroki = random.randint(1, len(kolo_fortuny))
    for j in range(kroki):
        kolo_fortuny.rotate(1)
        spinit(3)
        print(list(kolo_fortuny)) 

    print("Wygrałeś: ", kolo_fortuny[0][0])
