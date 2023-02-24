def S(x):
    return x + 1

def P(x):
    if x < 1:
        raise ValueError(
            f"{x} doesn't have a natural predecessor"
        )
    return x - 1

def add(a, b):
    for _ in range(b):
        a = S(a)
    return a

def sub(a, b):
    for _ in range(b):
        a = P(a)
    return a

def mul(a, b):
    result = 0
    for _ in range(b):
        result = add(result, a)
    return result

def fdiv(a, b):
    result = 0
    while a >= b:
        a = sub(a, b)
        result = S(result)
    return result

def mod(a, b):
    while a >= b:
        a = sub(a, b)
    return a

def pow(a, b):
    result = 1
    for _ in range(b):
        result = mul(result, a)
    return result
