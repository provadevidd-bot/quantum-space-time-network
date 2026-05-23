# Quantum Space-Time Network Simulation 🌌💻

**Autore:** Devid Castellani (Ricercatore Indipendente)  
**Co-Autore Computazionale:** Gemini AI (Google)

Questo repository contiene il formalismo matematico e il codice di simulazione per il modello di **Gravità Quantistica Informatica**. L'ipotesi centrale è che lo spaziotempo sia una proprietà macroscopica emergente dall'entanglement di una rete discreta di bit quantistici.

## 🧮 Formalismo Matematico
Il sistema è regolato dall'operatore di accoppiamento dinamico $\hat{\lambda}(\mathcal{R})$, che modula il flusso di informazione locale per risolvere la divergenza della densità energetica del vuoto:

$$\hat{\lambda}(\mathcal{R}) = \lambda_0 \cdot \oint_{\mathcal{R}} \frac{\partial \mathcal{I}(x)}{\partial t} dx \cdot \left[ 1 - \left( \frac{\mathcal{H}_{eff}}{\mathcal{H}_{Planck}} \right)^2 \right]$$

### Nomenclature del Modello
Per la descrizione completa dei parametri, fare riferimento alla sezione "Nomenclature" nel [PDF del Paper](link-al-tuo-pdf):
* **$J_{ij}$**: Matrice di accoppiamento (intensità dell'entanglement).
* **$M_i$**: Operatore di densità di informazione locale.
* **$R$**: Raggio di interazione.

## 🚀 Analisi Computazionale (Qiskit)
Il codice implementa il Grafo-Automa Quantistico.
- **Preparazione ($M_i$):** Le rotazioni `qc.rx` inizializzano la densità informativa locale.
- **Dinamica ($\hat{\lambda}(\mathcal{R})$):** Le porte `qc.crx` modulano l'entanglement tra i nodi della rete.
- **Validazione:** L'entropia di Von Neumann risultante funge da proxy per la metrica spaziotemporale emergente.

## 📄 Licenza e Riferimenti
L'opera è rilasciata sotto licenza **Creative Commons BY-NC-SA 4.0**.
Si prega di citare il paper originale (2026) in ogni ricerca derivata.
