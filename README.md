# Patient Health Dashboard

This project is a web-based dashboard for healthcare professionals to remotely monitor patient health data collected from a simple wristband device. The dashboard visualizes key health metrics, enabling early warnings and faster response times for patient care.

## Features

- **Remote Monitoring:** View patient data collected from wristbands in real time.
- **Health Metrics:** Track heart rate, steps, sleep hours, blood oxygen, and ECG waveforms.
- **Visual Insights:** Interactive charts and tables for trends and anomalies.
- **Early Warnings:** Highlights abnormal readings for quick intervention.
- **User-Friendly Interface:** Clean, responsive design for easy navigation.

## How It Works

1. **Wristband Device:** Patients wear a wristband that records health metrics and uploads data.
2. **Backend (Flask):** A Python Flask server reads patient data from `patient_data.csv` and serves it via a REST API.
3. **Frontend (HTML/JS):** The dashboard (`index.html`) fetches and visualizes the data, allowing healthcare professionals to select patients and review their health trends.

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone this repository or download the files.
2. Install Flask:
   ```sh
   pip install flask
   ```
3. Ensure `patient_data.csv` and `index.html` are in the same directory as the Flask app.

### Running the Dashboard

1. Start the Flask server:
   ```sh
   python "from flask import Flask, jsonify.py"
   ```
2. Open your browser and go to [http://localhost:5000](http://localhost:5000).

### File Structure

- `index.html` — Main dashboard UI.
- `patient_data.csv` — Sample patient data from wristbands.
- `from flask import Flask, jsonify.py` — Flask backend serving the dashboard and API.

## Usage

- Select a patient from the dropdown to view their health data.
- Review charts for heart rate, steps, sleep, blood oxygen, and ECG.
- Abnormal readings are highlighted for quick attention.

## Customization

- Add new patient data to `patient_data.csv` as needed.
- Modify the frontend or backend to support additional metrics or integrations.

## License

This project is provided for demonstration and educational purposes.

---

*Empowering healthcare professionals with timely, actionable patient insights.*
