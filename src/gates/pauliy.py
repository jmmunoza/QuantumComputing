import numpy as np

from ..qgate import QGate


class PauliY(QGate):
    def __init__(self):
        super().__init__(np.array([[0, -1j], [1j, 0]]))