def funk(a):
    n = a
    def second(b):
        nonlocal n
        n=n*b
        return f"{a*b} {n}"
    return second

d = funk(5)
print(d(5))
print(d(5))
print(d(5))
print(d(5))