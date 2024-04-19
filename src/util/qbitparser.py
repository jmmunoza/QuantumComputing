import numpy as np

from ..qbit import Qbit


def qbitsToVector(qbits: list[Qbit]):
    num_qubits = len(qbits)
    amplitudes = []

    for state in range(2**num_qubits):
        state_str = format(state, f'0{num_qubits}b')

        amplitude = 1 
        for i, qbit in enumerate(qbits):
            amplitude *= qbit.a if state_str[i] == '0' else qbit.b
            
        amplitudes.append(amplitude )
        
    return np.array(amplitudes)


def vectorToQbits(vector: np.ndarray):
    num_qubits = int(np.log2(len(vector)))
    qbits = []
    
    for state in range(num_qubits):
        amplitude = vector[state]
        

    
        a = np.sqrt(amplitude)
        b = np.sqrt(1 - amplitude)
        qbit = Qbit(a, b)
        qbits.append(qbit)
   
    return qbits