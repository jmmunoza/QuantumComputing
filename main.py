from src.algorithms.grover.grover import Grover
from src.algorithms.grover.oracle import Oracle

if __name__ == '__main__':
    circuit = Grover(Oracle(100), 8)

    circuit.draw()
