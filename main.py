from src.algorithms.grover.grover import Grover
from src.algorithms.grover.oracle import Oracle

if __name__ == '__main__':
    circuit = Grover(Oracle(13), 4)
    print(circuit)
    circuit.run()
    print(circuit)
    circuit.draw()
