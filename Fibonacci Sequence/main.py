def fibo(num):
    a, b = 0, 1
    yield a
    yield b
    for _ in range(num - 2):
        a, b = b, a + b
        yield b

for x in fibo(20):
    print(x)
