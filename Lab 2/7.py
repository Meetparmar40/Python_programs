def isprime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if not n % i:
            return False

    return True

for i in range (1, 21):
    if isprime(i):
        print(i)
