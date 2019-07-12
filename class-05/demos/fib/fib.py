def fib_finder(k):
    breakpoint()
    if k < 2:
        return k

    return fib_finder(k-1) + fib_finder(k - 2)

if __name__ == "__main__":
    fib_finder(5)


