import numpy as np


class QRegister:
    def __init__(self, n):
        self.n = n
        self.state = np.zeros(2**n, dtype=complex)
        self.state[0] = 1

    def __str__(self):
        return str(self.state)