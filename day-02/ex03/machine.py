import random
import beverages as bev

class CoffeeMachine:
    serve_num = 0

    def __init__(self):
        self.serve_num = 0

    class EmptyCup(bev.HotBeverage):
        name = "empty cup"
        price = 0.90

        def description(self):
            return ("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")


    def repair(self):
        self.serve_num = 0
        pass

    def serve(self, hot_bev):
        if self.serve_num == 10:
            raise CoffeeMachine.BrokenMachineException()
        
        self.serve_num += 1

        r = random.randrange(1000)
        if (r % 2 == 0):
            return (hot_bev)
        else:
            return (self.EmptyCup())

def work_machine(machine, drinks, n):
    i = 1
    while i <= n:
        try:
            print (machine.serve(drinks[random.randrange(4)]))
        except machine.BrokenMachineException as err :
            print(err)
        i += 1


def main():
    machine = CoffeeMachine()

    drinks = [bev.HotBeverage(), bev.Coffee(), bev.Tea(), bev.Chocolate(), bev.Cappuccino()]

    work_machine(machine, drinks, 11)
    machine.repair()
    work_machine(machine, drinks, 10)


if __name__ == '__main__':
    main()