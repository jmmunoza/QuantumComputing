class Qbit:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}|0> + {self.b}|1>'