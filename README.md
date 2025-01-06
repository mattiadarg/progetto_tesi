# Sistema Sicuro per il Monitoraggio della Frequenza Cardiaca

## Descrizione del Progetto
Questo progetto si inserisce nell'ambito dell'**Internet of Medical Things (IoMT)**, con l'obiettivo di creare un sistema avanzato e sicuro per il monitoraggio della frequenza cardiaca. La soluzione combina tecnologie hardware e software per garantire la raccolta e l'elaborazione dei dati biometrici, affrontando problematiche legate alla sicurezza informatica e alla privacy.

### Scopo del Progetto
- Creare un sistema sicuro e affidabile per il monitoraggio continuo della frequenza cardiaca.
- Garantire la protezione dei dati biometrici dei pazienti contro vulnerabilità di sicurezza e privacy.
- Fornire una base per l'espansione verso il monitoraggio di altri parametri vitali.

## Componenti Principali
### 1. **Hardware**
- **Samsung Artik**:
  - **Main Board**: Acquisizione dei dati biometrici.
  - **Interface Board**: Visualizzazione dei dati su schermo.
- **Sensori Biometrici**:
  - Sensore **MAX30102** per la rilevazione della frequenza cardiaca.

### 2. **Software**
- Librerie e strumenti utilizzati:
  - **Pybluez**: Gestione della comunicazione Bluetooth.
  - **Numpy**: Elaborazione numerica e manipolazione dei dati.
  - **Smbus**: Comunicazione I2C per interfacciarsi con i sensori.
  - **Lcd_i2c**: Gestione del display LCD.
  - **Hrcalc**: Calcolo della frequenza cardiaca.

### 3. **Sicurezza Informatica**
- **Sicurezza Hardware**:
  - Garanzia di autenticità del codice e archiviazione sicura delle chiavi.
  - Protezione contro manomissioni e intercettazioni.
- **Sicurezza Software**:
  - Crittografia dei dati per garantire la privacy del paziente.

## Sviluppi Futuri
Il sistema potrà essere esteso per monitorare altri parametri vitali, tra cui:
- Pressione arteriosa.
- Temperatura corporea.
- Frequenza respiratoria.
- Ossigenazione del sangue.

## Vantaggi
- **Efficienza**: Monitoraggio continuo e affidabile dei dati biometrici.
- **Sicurezza**: Implementazione di tecnologie hardware avanzate per proteggere i dati.
- **Scalabilità**: Possibilità di espandere il sistema con nuove funzionalità.

## Autore
**Mattia d’Argenio**

Per domande o suggerimenti, non esitare a contattarmi.

---
