from ...gates.gdiffuser import GDiffuser
from ...qcircuit import QCircuit
from ...qgate import QGate


class Grover(QCircuit):
    def __init__(self, oracle: QGate, n_qbits: int, n_iterations: int = 1):
        super().__init__(n_qbits, "Grover")

        self.h(range(len(self.qbits)))

        for _ in range(n_iterations):
            
            # Apply the oracle
            self.oracle()
            
            # Apply the Grover diffusion operator
           # self.grover_diffusion()

    def oracle(self):
        n_qbits = len(self.qbits)
        
        self.h(0)
        self.h(0)
        
#        self.cx(range(n_qbits))
    
    def grover_diffusion(self): 
        n_qbits = len(self.qbits)
        
        self.h(range(n_qbits))
        self.x(range(n_qbits))
        self.h(-1)
        self.cx(range(n_qbits))
        self.h(-1)
        self.x(range(n_qbits))
        self.h(range(n_qbits))
        
