import sys
import os
import time
from threading import Thread

print(sys.executable)

y = os.getenv("PYTHONIOENCODING")
print("PYTHONIOENCODING is : ", y)

z = os.getenv("test")
print("test is : ", z)


def calc_cube(numbers: list) -> None:
    print("calculating cube numbers")
    for i in numbers:
        time.sleep(0.2)
        print("cube ", i * i * i)


def calc_square(numbers: list) -> None:
    print("calculating square numbers")
    for i in numbers:
        time.sleep(0.2)
        print("square ", i * i)


values = [2, 3, 8, 9]

time_start = time.time()

t1 = Thread(target=calc_cube, args=(values,))
t2 = Thread(target=calc_square, args=(values,))

t1.start()
t2.start()

t1.join()
t2.join()

# calc_square(values)
# calc_cube(values)

print("Time performed : ", time.time() - time_start)
