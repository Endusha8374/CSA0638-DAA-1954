def is_palindrome(s):
    s = s.lower()  # Convert string to lowercase for case-insensitive comparison
    # Base cases:
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    # Recursive case:
    return is_palindrome(s[1:-1])

# Example usage:
input_string = "level"
if is_palindrome(input_string):
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
