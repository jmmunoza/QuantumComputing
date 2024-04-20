from src.algorithms.grover.grover import Grover
from src.algorithms.grover.oracle import Oracle

if __name__ == '__main__':
    grover = Grover(Oracle(63), 6)
    grover.run()
    grover.draw()
