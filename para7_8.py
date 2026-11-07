def checker(func, *args, **kwargs):
    try:
        result = Func(*args, **kwargs)
    except  Exception as exc:
        print(f"We have problems{exc}")
    else:
        print(f"No problems. Result = {result}")
@checker
def calculate(expression):
    return eval(expression)


calc = checker(calculate)
calculate("2+2")
