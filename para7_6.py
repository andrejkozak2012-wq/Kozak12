class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, new_work):
        return f"I will hlp you wth your {self.work}." \
               f"Afterweards i will help you with {new_work}"


helper = Helper("homework")
print(helper("cleaning"))


