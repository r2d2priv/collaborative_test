# This function expects a str and returns a str
def is_palindrome(word: str) -> str:
    return ("is palindrome" if (word[::-1]==word) else "is not palindrome")