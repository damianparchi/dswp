import random
from array import array


tab = sorted(array('I', [random.randint(0,1000) for _ in range(100)]))
print(tab[len(tab):len(tab)-int(len(tab)/10)-1:-1])
