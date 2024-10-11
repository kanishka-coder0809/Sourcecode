# Function to check if a string is a palindrome
def is_palindrome(s):
    # Convert the string to lowercase to make it case insensitive
    s = s.lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# Input from the user
string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
