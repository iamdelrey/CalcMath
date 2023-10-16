def f(x):
    return x**3 + 3.63 * x**2 - x - 3.63

def df(x):
    return 3 * x**2 + 7.26 * x - 1

def newton_method(initial_guess, epsilon):
    x0 = initial_guess
    x1 = x0 - f(x0) / df(x0)
    iterations = 1

    while abs(x1 - x0) >= epsilon:
        print(f"Iteration {iterations}: x = {x0}, |x1 - x0| = {abs(x1 - x0)}")
        x0 = x1
        x1 = x0 - f(x0) / df(x0)
        iterations += 1

    return x1, iterations

initial_guess = 2.0
epsilon = 1e-3

root, iterations = newton_method(initial_guess, epsilon)
print(f"Корень уравнения: {root}")
print(f"Количество итераций: {iterations}")