"""
Flask Web Application for Medical Expert System
"""

from flask import Flask, render_template, request, jsonify
from expert_system import ExpertSystem
from datetime import datetime

app = Flask(__name__)
expert_system = ExpertSystem()

@app.route('/')
def index():
    symptoms = expert_system.get_symptoms()
    return render_template('index.html', symptoms=symptoms)

@app.route('/diagnose', methods=['POST'])
def diagnose():
    try:
        data = request.get_json()
        patient_name = data.get('patient_name', '').strip()
        selected_symptoms = data.get('symptoms', [])
        
        if not patient_name:
            return jsonify({
                'success': False,
                'message': 'Please enter patient name'
            }), 400
        
        if not selected_symptoms:
            return jsonify({
                'success': False,
                'message': 'Please select at least one symptom'
            }), 400
        
        selected_symptom_ids = [int(sid) for sid in selected_symptoms]
        result = expert_system.diagnose(selected_symptom_ids)
        symptom_names = expert_system.get_symptom_names(selected_symptom_ids)
        
        return jsonify({
            'success': True,
            'patient_name': patient_name,
            'selected_symptoms': symptom_names,
            'diagnosis': result,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'Error: {str(e)}'
        }), 500

if __name__ == '__main__':
    print("=" * 60)
    print("🏥 MEDICAL EXPERT SYSTEM - AI DIAGNOSIS")
    print("=" * 60)
    print("✅ Server starting...")
    print("📍 Open your browser at: http://localhost:5000")
    print("📍 Or on your network at: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)