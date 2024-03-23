def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Test the function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)
print("GCD of", num1, "and", num2, "is", result)
