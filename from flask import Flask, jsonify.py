from flask import Flask, jsonify, send_from_directory
import csv
import os
import ast

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/api/patient-data')
def patient_data():
    data = []
    with open('patient_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Parse ecg_waveform as a list if present
            if 'ecg_waveform' in row and row['ecg_waveform']:
                try:
                    row['ecg_waveform'] = ast.literal_eval(row['ecg_waveform'])
                except Exception:
                    row['ecg_waveform'] = []
            data.append(row)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)