import numpy as np

from ..qgate import QGate


class PauliZ(QGate):
    def __init__(self):
        super().__init__(np.array([[1, 0], [0, -1]]))