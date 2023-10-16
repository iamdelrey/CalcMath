def f(x):
    return x**3 - 4.5*x +1.9


#a = -2.551
#b = -4.63

print("Введите левую границу: ")
a = int(input())
print("Введите правую границу: ")
b = int(input())
epsilon = 1e-3


def simple_iteration_method(f, a, b, eps):
    x = a  # Используем левую границу интервала как начальное приближение
    iterations = 0

    while True:
        f_x = f(x)  # Вычисляем f(x) для текущего x
        x_new = x - f_x * (b - a) / (f(b) - f(a))
        iterations += 1
        condition_result = f(x_new - eps) * f(x_new + eps)
        print(f"Iteration {iterations}: x = {x}, f(x) = {f_x}, x_new = {x_new}, Condition Result = {condition_result}")

        if abs(x_new - x) < eps:
            # Проверяем условие для завершения итераций
            if condition_result < 0:
                return x_new, iterations
            else:
                raise Exception("Условие для завершения итераций не выполняется.")
        x = x_new


try:
    result, iterations = simple_iteration_method(f, a, b, epsilon)
    print(f"Приближенное значение корня: {result}")
    print(f"Количество операций (итераций): {iterations}")
except Exception as e:
    print(f"Ошибка: {e}")