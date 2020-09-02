import os
import time
import multiprocessing
from typing import Callable



def time_it(func: Callable) -> Callable:
    def timed_func():
        start_time = time.time()
        func()
        end_time = time.time()
        delta = end_time - start_time
        print(f">>> Execution took {round(delta, 5)}s")

    return timed_func

def calculate(x):
    time.sleep(1)
    return (x**x)**2 + 10


data = [1,2,3,4,5,6,7,8,9,10]

@time_it
def normal():
    result = map(calculate, data)
    print(list(result))

@time_it
def parallel():
    cpu_count = os.cpu_count()
    print(f">>> CPU Count: {cpu_count}")

    pool = multiprocessing.Pool()
    result = pool.map(calculate, data)
    print(list(result))

if __name__ == "__main__":
    normal()
    parallel()
