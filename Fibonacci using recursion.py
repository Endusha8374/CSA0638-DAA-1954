def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(count):
    if count <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Series:")
        for i in range(count):
            print(fibonacci(i), end=" ")

# Taking input from the user for the count of numbers in the series
try:
    count = int(input("Enter the count of Fibonacci numbers to print: "))
    print_fibonacci_series(count)
except ValueError:
    print("Please enter a valid integer.")
