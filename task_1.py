def caching_fibonacci():
    fib_num = {0: 0, 1: 1}

    def fibonacci(n):
        nonlocal fib_num
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n in fib_num:
                return fib_num[n]
            fib_num[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return fib_num[n]

    return fibonacci


def main():
    usrinput = int(input("Fibonacci number: "))

    fibo_func = caching_fibonacci()
    print(fibo_func(usrinput))


if __name__ == '__main__':
    main()
