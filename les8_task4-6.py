# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

# Склад оргтехники
class Storage:
    print('Склад оргтехники')


# Оргтехника
class OfficeTech:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power


class Computer(OfficeTech):
    computer_amt = 0

    def __init__(self, brand, ram, power):
        super().__init__(brand, ram)
        self.power = power
        self.ram = ram

        Computer.computer_amt += 1

    @staticmethod
    def name():
        return 'Системный блок: '

    def power_of_computer(self):
        return self.power

    def __str__(self):
        return '\tПроизводитель: {} \tОперативная память: {} \tПотребляемая мощность: {}'.format(self.brand, self.ram,
                                                                                                 self.power)


class Monitor(OfficeTech):
    monitor_amt = 0

    def __init__(self, brand, diagonal, power):
        super().__init__(brand, diagonal)
        self.power = power
        self.diagonal = diagonal

        Monitor.monitor_amt += 1

    @staticmethod
    def name():
        return 'Монитор: '

    def power_of_monitor(self):
        return self.power

    def __str__(self):
        return '\tПроизводитель: {} \tДиагональ экрана: {} \tПотребляемая мощность: {}'.format(self.brand,
                                                                                               self.diagonal,
                                                                                               self.power)


class Laptop(OfficeTech):
    laptop_amt = 0

    def __init__(self, brand, ram, power):
        super().__init__(brand, ram)
        self.power = power
        self.ram = ram

        Laptop.laptop_amt += 1

    @staticmethod
    def name():
        return 'Ноутбук: '

    def power_of_laptop(self):
        return self.power

    def __str__(self):
        return '\tПроизводитель: {} \tОперативная память: {} \tПотребляемая мощность: {}'.format(self.brand, self.ram,
                                                                                                 self.power)


class Printer(OfficeTech):
    printer_amt = 0

    def __init__(self, brand, color, power):
        super().__init__(brand, color)
        self.power = power
        self.color = color

        Printer.printer_amt += 1

    @staticmethod
    def name():
        return 'Принтер: '

    def power_of_printer(self):
        return self.power

    def __str__(self):
        return '\tПроизводитель: {} \tЦвет принтера: {} \tПотребляемая мощность: {}'.format(self.brand, self.color,
                                                                                            self.power)


class Scanner(OfficeTech):
    scanner_amt = 0

    def __init__(self, brand, color, power):
        super().__init__(brand, color)
        self.power = power
        self.color = color

        Scanner.scanner_amt += 1

    @staticmethod
    def name():
        return 'Сканер: '

    def power_of_scanner(self):
        return self.power

    def __str__(self):
        return '\tПроизводитель: {} \tЦвет сканера: {} \tПотребляемая мощность: {}'.format(self.brand, self.color,
                                                                                           self.power)


c_1 = Computer('Acer Veriton X2665G', '8 ГБ', '180 Вт')
c_2 = Computer('Lenovo 310S-08IGM', '4 ГБ', '160 Вт')
c_3 = Computer('Lenovo T540-15ICB G', '8 ГБ', '190 Вт')
print(c_1.name(), c_1.computer_amt, 'шт')
# print(c_1.__str__(), c_2.__str__(), c_3.__str__())
print(c_1.__str__())
print(c_2.__str__())
print(c_3.__str__())

m_1 = Monitor('LG 25UM58', '25', '25 Вт')
m_2 = Monitor('Xiaomi Mi Display', '23.8', '24 Вт')
m_3 = Monitor('Samsung C32F391FWI', '31.5', '35 Вт')
print(m_1.name(), m_1.monitor_amt, 'шт')
print(m_1.__str__())
print(m_2.__str__())
print(m_3.__str__())

l_1 = Laptop('ASUS VivoBook X512', '4 ГБ', '75 Вт')
l_2 = Laptop('HUAWEI MateBook', '8 ГБ', '80 Вт')
l_3 = Laptop('Apple MacBook Pro 13 Mid 2020', '8 ГБ', '60 Вт')
l_4 = Laptop('Apple MacBook Pro 13 Mid 2020', '8 ГБ', '60 Вт')
l_5 = Laptop('Apple MacBook Pro 13 Mid 2020', '8 ГБ', '60 Вт')
print(l_1.name(), l_1.laptop_amt, 'шт')
print(l_1.__str__())
print(l_2.__str__())

p_1 = Printer('Canon i-SENSYS LBP6030B', 'Черный', '870 Вт')
p_2 = Printer('Xerox Phaser 3020BI', 'Белый', '313 Вт')
p_3 = Printer('HP Laser 107w', 'Белый', '320 Вт')
print(p_1.name(), p_1.printer_amt, 'шт')
print(p_1.__str__())
print(p_2.__str__())
print(p_3.__str__())

s_1 = Scanner('Canon CanoScan LiDE 400', 'Черный', '4.5 Вт')
s_2 = Scanner('Epson Perfection V19', 'Черный', '2.5 Вт')
print(s_1.name(), s_1.scanner_amt, 'шт')
print(s_1.__str__())
print(s_2.__str__())
