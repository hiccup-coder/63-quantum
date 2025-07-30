
import cirq
from cirq.contrib.qasm_import import circuit_from_qasm
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import qsimcirq

import numpy as np
import time

# For test
from tests.qasm import test_qasm1

test_qasm2 = """
OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
h q[0];
cx q[0], q[1];
cx q[1], q[2];
s q[2];
h q[2];
"""

def calc_option1():

    print("Option 1--------------------------------")
    start_time = time.time()

    # Convert QASM string to Cirq Circuit
    circuit = circuit_from_qasm(test_qasm1)

    print(f"Circuit Elapsed Time: {time.time() - start_time}")

def calc_option2():
    print("Option 2--------------------------------")
    start_time = time.time()

    circuit = QuantumCircuit.from_qasm_str(test_qasm1)
    print(f"Circuit Elapsed Time: {time.time() - start_time}")
    
    start_time = time.time()
    circuit_no_meas = circuit #circuit_no_meas = circuit.remove_final_measurements(inplace=False) # 

    backend_sv = AerSimulator(method="statevector", device="CPU", max_parallel_experiments=16, max_parallel_threads=16, blocking_enable=True)
    circuit_no_meas.save_statevector()  # type: ignore
    job = backend_sv.run(circuit_no_meas)
    result = job.result()
    # statevector = result.data(0)["statevector"]

    print(f"StateVector Elapsed Time: {time.time() - start_time}")
    # print(np.array(statevector))
    print(result)

calc_option1()
calc_option2()

