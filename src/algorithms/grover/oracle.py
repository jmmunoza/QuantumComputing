import numpy as np

from ...qbit import Qbit
from ...qgate import QGate
from ...util.qbitparser import qbitsToVector


class Oracle(QGate):
    def __init__(self, value: int):
        super().__init__(None)
        self.value = value 
        
    def apply(self, state: list[Qbit]):
        self.matrix = np.identity(2**len(state))
        
        for i in range(2**len(state)):
            if i == self.value:
                self.matrix[i, i] = -1
                
        statevector = qbitsToVector(state)
        statevector = np.dot(self.matrix, statevector)
        
        for i, qbit in enumerate(state):
            qbit.a = statevector[2*i]
            qbit.b = statevector[2*i + 1]
      
        return state
    
    def __str__(self):
        return "Oracle"