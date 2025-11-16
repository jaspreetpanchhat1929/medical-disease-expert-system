"""
Medical Expert System - Rule-Based AI Engine
Implements forward chaining inference for disease diagnosis
"""

class ExpertSystem:
    def __init__(self):
        # Define symptoms
        self.symptoms = {
            1: {"name": "Fever", "description": "Rise in body temperature above normal"},
            2: {"name": "Chills", "description": "Sensation of coldness with shivering"},
            3: {"name": "Sweating", "description": "Excessive sweating often following fever"},
            4: {"name": "Headache", "description": "Continuous pain in the head or forehead"},
            5: {"name": "Fatigue", "description": "Feeling of tiredness or weakness"},
            6: {"name": "Abdominal Pain", "description": "Discomfort or cramps in the stomach area"},
            7: {"name": "Loss of Appetite", "description": "Reduced desire to eat"},
            8: {"name": "Diarrhea", "description": "Frequent loose or watery bowel movements"},
            9: {"name": "Body Pain", "description": "Pain in muscles and joints"},
            10: {"name": "Nausea", "description": "Feeling of sickness or urge to vomit"}
        }
        
        # Define diseases with rules
        self.diseases = {
            "Malaria": {
                "id": 1,
                "description": "A mosquito-borne disease caused by Plasmodium parasite, resulting in fever and chills.",
                "recommendation": "Get a malaria blood test; take prescribed anti-malarial drugs; rest and stay hydrated.",
                "required_symptoms": [1, 2, 3],
                "optional_symptoms": [5, 9],
                "color": "danger"
            },
            "Typhoid": {
                "id": 2,
                "description": "A bacterial infection caused by Salmonella typhi, spreading through contaminated food and water.",
                "recommendation": "Get a Widal test; take antibiotics as prescribed; maintain hygiene and hydration.",
                "required_symptoms": [1, 4, 6, 7],
                "optional_symptoms": [8, 10],
                "color": "warning"
            }
        }
    
    def get_symptoms(self):
        return self.symptoms
    
    def diagnose(self, selected_symptom_ids):
        if not selected_symptom_ids:
            return {"detected": [], "message": "Please select at least one symptom"}
        
        detected_diseases = []
        
        for disease_name, disease_info in self.diseases.items():
            required_match = all(
                symptom_id in selected_symptom_ids 
                for symptom_id in disease_info["required_symptoms"]
            )
            
            if required_match:
                optional_match_count = sum(
                    1 for symptom_id in disease_info["optional_symptoms"]
                    if symptom_id in selected_symptom_ids
                )
                
                total_symptoms = len(disease_info["required_symptoms"]) + len(disease_info["optional_symptoms"])
                matched_symptoms = len(disease_info["required_symptoms"]) + optional_match_count
                
                confidence = round((matched_symptoms / total_symptoms) * 100)
                
                detected_diseases.append({
                    "name": disease_name,
                    "description": disease_info["description"],
                    "recommendation": disease_info["recommendation"],
                    "confidence": confidence,
                    "color": disease_info["color"]
                })
        
        detected_diseases.sort(key=lambda x: x["confidence"], reverse=True)
        
        return {
            "detected": detected_diseases,
            "message": "Diagnosis completed successfully" if detected_diseases else "No disease detected"
        }
    
    def get_symptom_names(self, symptom_ids):
        return [self.symptoms[sid]["name"] for sid in symptom_ids if sid in self.symptoms]