try:
    print("Start")
    print(10/0)
    print("No errors")
except NameError:
    print("We have an error")
except ZeroDivisionError:
    print("We have an zero error")

print("code after capsule")
