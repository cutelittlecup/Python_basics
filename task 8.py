import requests
import time
import re


BOOK_PATH = 'https://www.gutenberg.org/files/2638/2638-0.txt'


def benchmark(func):
    """
    The decorator that outputs the time it took to execute the decorated function
    """

    def wrapper(*args, **kwargs):

        time_start = time.time()
        func(*args, **kwargs)
        print(f'Function execution time: {time.time() - time_start} sec')

        return func(*args, **kwargs)

    return wrapper


def logging(func):
    """
    The decorator that outputs the parameters with which the function was called
    """

    def wrapper(*args, **kwargs):
        print(f'The function is called with parameters: {args}, {kwargs}')
        return func(*args, **kwargs)

    return wrapper


def counter(func):
    """
    The decorator that counts and outputs the number of calls to the function being decorated
    """

    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f'The function is called {wrapper.calls} times')
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@counter
@logging
@benchmark
def word_count(word, url=BOOK_PATH):
    """
    Function for counting the specified word on a html page
    """

    raw = requests.get(url).text

    processed_book = re.sub('[\W]+' , ' ', raw).lower()

    cnt = len(re.findall(word.lower(), processed_book))

    return f"The word {word} occurs {cnt} times\n\n"


print(word_count('whole'))
print(word_count('is'))
print(word_count('and'))
