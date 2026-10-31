try:
    print("Start")
    print(10 / 0)
    print("No errors")
except NameError:
    print("We have an error")
except (ZeroDivisionError, ZeroDivisionError):

    print("code after capsule")
