def f(x):
    return x**3 - 4.5*x + 1.9

def chord_method(a, b, tol):
    i = 0  # Номер итерации
    while True:
        next_a = a - f(a) * (b - a) / (f(b) - f(a))
        diff = abs(next_a - a)
        if(i == 0):
            print(f"x0: {a}, |next_a - a|: {diff}")
        else:
            print(f"Итерация {i}: x: {a}, |next_a - a|: {diff}")
        if diff < tol:
            return next_a
        a = next_a
        i += 1

a = 0  # левая граница интервала
b = 1  # правая граница интервала
tolerance = 1e-3  # желаемая точность (10^-3)

result = chord_method(a, b, tolerance)
print("Корень уравнения:", result)