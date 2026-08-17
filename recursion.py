def Sum(n):
    if n == 0:
        return n;
    return n + Sum(n - 1)

print(Sum(8))