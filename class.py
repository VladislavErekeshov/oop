class Robot:
    '''Представляет робота с именем'''
    #переменная класса, содержащая количество роботов
    population = 0

    def __init__(self, name):
        '''Инициализация данных'''
        self.name = name
        print("инициализация {0}".format(self.name))
        #при создании этой личности робот добавляется
        #к переменной population
        Robot.population += 1

    def __del__(self):
        '''я умираю'''
        print("{0} уничтожается".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{0} был последним".format(self.name))
        else:
            print("осталось {0:d} работающих роботов".format(Robot.population))

    def sayHi(self):
        print("Пориветствую, мои хозяева, называйте меня {0}".format(self.name))

    def howmany():
        print("у нас осталось {0:d} роботов".format(Robot.population))

droid1 = Robot("R2-D2")
droid1.sayHi()
Robot.howmany()

droid2 = Robot("C-3PO")
droid2.sayHi()
Robot.howmany()

print("\nЗдесь роботы могут делать какую-то работу.\n")

print("Роботы закончили свою работу, давайте уничтожим их")

del droid1
del droid2

Robot.howmany()
