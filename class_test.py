class Greeter:
    MY_VAR = "HEY"

    def hello(self, name: str):
        print(f"{self.MY_VAR} {name}")


x = Greeter
x.hello("james")