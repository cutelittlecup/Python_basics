import string


def solution(a_string: str) -> bool:
    """
    Reverse the string and check is it a palindrome or not

    :param a_string: string to check
    :return: False/True as an answer on the question palindrome is string or not
    """
    a_string = ''.join(c for c in a_string if c not in string.punctuation and c != ' ').lower()
    return a_string == a_string[::-1]


new_string = input('Enter a string:')

print(f"String '{new_string}' is palindrome: {solution(new_string)}")
