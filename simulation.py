import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector, entropy

def esegui_stress_test_cosmico(lambda_param):
    """
    Simula l'evoluzione di una rete di spaziotempo quantistico a 4 nodi.
    Verifica la stabilità entropica del sistema.
    """
    # Inizializzazione dei nodi (qubit)
    qc = QuantumCircuit(4)
    
    # Stato primordiale: creazione della sovrapposizione quantistica
    for i in range(4):
        qc.rx(np.pi / 4, i)
        
    # Applicazione dell'operatore di scambio (Entanglement generatore di spazio)
    angolo_interazione = lambda_param * np.pi / 2
    qc.crx(angolo_interazione, 0, 1)
    qc.crx(angolo_interazione, 1, 2)
    qc.crx(angolo_interazione, 2, 3)
    qc.crx(angolo_interazione, 3, 0) # Chiusura topologica ad anello
    
    # Estrazione dello stato d'onda finale
    stato_matrice = Statevector.from_instruction(qc)
    
    # Calcolo dell'entropia di Von Neumann del sistema integrato
    entropia_calcolata = entropy(stato_matrice)
    
    return entropia_calcolata, stato_matrice

# Validazione numerica nella zona Goldilocks (Sezione Aurea)
lambda_test = 0.618033
entropia_finale, _ = esegui_stress_test_cosmico(lambda_test)

print(f"--- RISULTATI DELLA SIMULAZIONE QUANTISTICA ---")
print(f"Parametro Lambda impostato: {lambda_test}")
print(f"Entropia di Von Neumann registrata sulla rete: {entropia_finale:.6f} bit.")
print(f"Stato quantistico dello Spaziotempo emergente calcolato con successo.")

