from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n < 1:
        return "Number must be greater than 0"
    elif not isinstance(n, int):
        return "Enter a valid integer"
    else:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif n > 2:
            return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def compareTo(a, b):
    if len(a) == 0 and len(b) == 0:
        return 0
    elif len(a) == 0:
        return -1
    elif len(b) == 0:
        return 1
    elif a[0] > b[0]:
        return 1
    elif a[0] < b[0]:
        return -1
    else:
        return compareTo(a [1:], b[1:])

if __name__ == "__main__":
    print(fibonacci(20))
    print(gcd(60, 48))
    print(compareTo("hello", "hello"))
    print(compareTo("Hello", "hello"))
