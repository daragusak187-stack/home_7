def calculator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            print(f"Результат: {result}")
            return result
        except ZeroDivisionError:
            print("Помилка: Ділення на нуль ❌")
        except SyntaxError:
            print("Помилка: Неправильний вираз ⚠️")
        except NameError:
            print("Помилка: Невідомі символи ⚠️")
        return None
    return wrapper


@calculator
def calculate(expression):
    return eval(expression)

while True:
    a = input("Введіть перше число (або 'exit' для виходу): ")
    if a.lower() == "exit":
        break
    b = input("Введіть друге число: ")
    op = input("Введіть дію (+, -, *, /): ")

    vidpovid = f"{a}{op}{b}"
    calculate(vidpovid)
