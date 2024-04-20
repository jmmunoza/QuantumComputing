import numpy as np

from ..qgate import QGate


class Hadamard(QGate): 
    def __init__(self):
        super().__init__(np.array([[1, 1], [1, -1]]) / np.sqrt(2))