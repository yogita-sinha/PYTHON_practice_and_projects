import re

def is_palindrome(s):
    s = re.sub(r'[^a-z0-9]', '', s.lower())

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# Test
s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))