def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    fib = [0, 1]
    
    for _ in range(2, length):
        fib.append(fib[-1] + fib[-2])
    
    print(fib[:length])
