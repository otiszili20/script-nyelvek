import math
from types import FunctionType
import logging
import time

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='decorator.log',
                    filemode='w',
                    format=LOG_FORMAT,
                    level=logging.DEBUG)
LOGGER = logging.getLogger()


def say_hello(name: str) -> None:
    print(f'Hello {name}!')


def power(base: float) -> FunctionType:
    """
    Currying is
    :param base:
    :return:
    """
    def currying_function(power: float) -> float:
        return math.pow(base, power)
    return currying_function


def counter(init_value: int = 1, step: int = 1) -> FunctionType:
    """
    Closure Example
    :param init_value:
    :param step:
    :return:
    """
    count = init_value

    def increment() -> int:
        nonlocal count
        count += step
        return count
    return increment


def count_n_times(n: int, counter_callback) -> None:
    for _ in range(n):
        print(f'{counter_callback()}')


def uppercase_decorator(function):
    def wrapper():
        answer = function()
        uppercase_answer = answer.upper()
        return uppercase_answer
    return wrapper()


def log_function_call(function):
    def wrapper(*args, **kwargs):
        LOGGER.info(f'{function.__name__} has been called')
        result = function(*args, **kwargs)
        LOGGER.info(f'{function.__name__} has been finished')
        return result
    return wrapper


def measure_execution_time(function):
    def wrapper(*args, **kwargs):
        start_timestamp = time.time()
        result = function(*args, **kwargs)
        end_timestamp = time.time()
        LOGGER.info(f'Execution time of {function.__name__} was {round((end_timestamp - start_timestamp) * 1000, 1)}s')
        return result
    return wrapper


if __name__ == '__main__':
    print('Hello World')
    say_hello('Python')
    function_pointer = say_hello
    function_pointer('Function Pointer')
    print(f'Using Currying to Calculate 2^10= {power(2)(10)}')

    print('Counter Closure Example')
    my_counter = counter(0,10)
    print(f'{my_counter()}')
    print(f'{my_counter()}')
    print(f'{my_counter()}')
    print('Using Callback Functions!')
    count_n_times(5,my_counter)

    def get_hello_msg():
        return 'Hello'

    print(f'{uppercase_decorator(get_hello_msg)}')
    print(f'{uppercase_decorator(lambda: "World")}')

    @measure_execution_time
    @log_function_call
    def sleepy_function(seconds: int) -> None:
        time.sleep(seconds)

    sleepy_function(3)

    sum = lambda x, y: x+y
    print(f'Sum of 3 and 5 is {sum(3,5)}')

    numbers = [x for x in range(10)]
    print(f'{list(map(lambda x: x ** 2, numbers))}')
    print(f'Evens = {list(filter(lambda x: x % 2 == 0, numbers))}')
