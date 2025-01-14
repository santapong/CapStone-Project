import time
from typing import Optional

# NOTE: This func make for monitor request time.
# Create decorator for timer.
def timer(func):
    def wrapper(args):
        start_process = time.time()
        func(args)
        time_usage = time.time() - start_process
        print(time_usage)

    return wrapper


# Using for test
@timer
def test(number:Optional[int]=10000):
    for i in range(0 ,number):
        print("Hello")

if __name__ == '__main__':
    test(100000)



