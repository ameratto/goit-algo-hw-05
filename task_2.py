import re
from typing import Callable, Generator, Any


def num_generator_logger(func):
    def checking(*args):
        if not args:
            print("Warning! String is empty")
            return False
        else:
            return func(*args)

    return checking


@num_generator_logger
def generator_numbers(string) -> Generator[float, Any, None]:
    pattern = r' \d+[.]\d* '
    for find_pattern in re.findall(pattern, string):
        yield float(find_pattern)


@num_generator_logger
def sum_profit(string: str, func: Callable[[str], float]):
    total_incal = 0.0
    for number in func(string):
        total_incal += number
    return total_incal


def main():
    # x = """
    # Загальний дохід працівника складається з декількох частин:
    # 1000.01 як основний дохід, доповнений додатковими
    # надходженнями 27.45 і 324.00 доларів.
    # """
    x = "Загальний дохід працівника складається з декількох частин:"

    if not x:
        print("Something went wrong")
    else:
        for num in generator_numbers(x):
            print(f"num: {num}")
        print(f"Total income: {sum_profit(str(x), generator_numbers)}")


if __name__ == '__main__':
    main()
