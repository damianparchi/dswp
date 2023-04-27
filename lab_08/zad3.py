from collections import deque
import timeit

# pomiar czasu dla deque
setup = "from collections import deque"
stmt1 = "d = deque(); [d.append(i) for i in range(1000)]"
stmt2 = "d = deque(); [d.appendleft(i) for i in range(1000)]"
print("Deque - append:")
print(timeit.timeit(stmt1, setup=setup, number=10000))
print("Deque - appendleft:")
print(timeit.timeit(stmt2, setup=setup, number=10000))

# pomiar czasu dla list
setup = ""
stmt1 = "l = []; [l.append(i) for i in range(1000)]"
stmt2 = "l = []; [l.insert(0, i) for i in range(1000)]"
print("List - append:")
print(timeit.timeit(stmt1, setup=setup, number=10000))
print("List - insert(0):")
print(timeit.timeit(stmt2, setup=setup, number=10000))
