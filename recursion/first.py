
def matryoshka(n):
    if n == 1:
        print('Матрешка')
    else:
        print('Верх матрешки n=', n)
        matryoshka(n-1)
        print('Низ матрешки n=', n)


def factorial(n):

    if n == 0:
        return 1

    return factorial(n - 1) * n


def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)


def gcd_second(a, b):

    if b == 0:
        return a
    else:
        return gcd_second(b, a % b)

def pow(a, n):
    if n == 0:
        return 1
    else:
        return pow(a, n - 1) * a

def pow_second(a, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return pow(a, n - 1) * a
    else:
        return pow(a ** 2, n//2)


if __name__ == "__main__":
    matryoshka(4)
    print(factorial(3))
    print(gcd(12, 3))
    print(gcd_second(12, 3))
    print(pow(2, 20))
    print(pow_second(2, 20))