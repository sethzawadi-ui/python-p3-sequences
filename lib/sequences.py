def print_fibonacci(length):
    # If length is 0, print empty list
    if length == 0:
        print([])
        return

    # Start Fibonacci list
    fib = [0]

    # If length is 1, print [0]
    if length == 1:
        print(fib)
        return

    # Add the second number
    fib.append(1)

    # Generate the remaining numbers
    for i in range(2, length):
        fib.append(fib[-1] + fib[-2])

    # Print the entire list on one line
    print(fib)
