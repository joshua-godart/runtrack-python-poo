
class Operation:
    def __init__(self):
        self.number1 = 12
        self.number2 = 3

    def show_info(self):
        print("Le nombre1 est", self.number1)
        print("Le nombre2 est", self.number2)

    def addition(self):
        print("Le résultat de l'addition est",(self.number1 + self.number2))


operation = Operation()
operation.addition()