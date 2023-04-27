from collections import Counter, deque

def create_kolo_fortuny(*args):
    return deque(Counter(args).elements()) 


print(create_kolo_fortuny(5, 6, 6, 6, 2, 1, 3, 1 , 8, 2, 5, 1, 5))
