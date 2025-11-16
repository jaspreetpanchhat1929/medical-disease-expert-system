🩺 Smart Health Diagnosis System
AI-Powered Rule-Based Expert System for Early Disease Detection
This project is a modern Medical Expert System built using Python Flask.
It analyzes patient symptoms using a rule-based inference engine and provides an early diagnosis for Malaria and Typhoid, along with recommendations.

The system includes a clean and responsive UI to provide a real medical-app experience.

🚀 Features
✔ Rule-Based AI Diagnosis

✔ Forward-Chaining Inference Engine

✔ Professional UI (Flask + HTML/CSS)

✔ Confidence Score Calculation

✔ Dynamic Symptom Selection

✔ Patient Report Page

✔ Easy to Add More Symptoms & Diseases

📁 Project Structure
sql
Copy code
medical-disease-expert-system/
│── app.py
│── diseases.csv
│── symptoms.csv
│── rules.csv
│── patients.csv
│── static/
│     └── style.css
│── templates/
│     ├── index.html
│     └── result.html
│── README.md
🛠️ Technologies Used
Python Flask

HTML5 / CSS3

Bootstrap UI Cards

Rule-Based AI Logic

Pandas (optional)

Jinja2 Templates

🔍 How It Works
1️⃣ User enters their name
2️⃣ Selects symptoms from the list
3️⃣ The inference engine matches rules:
nginx
Copy code
IF Fever AND Chills AND Sweating THEN Malaria
IF Fever AND Headache AND Abdominal Pain THEN Typhoid
4️⃣ Confidence Score is calculated
5️⃣ Final Diagnosis + Recommendation is displayed
▶️ Running the Project
Install Dependencies
bash
Copy code
pip install flask pandas
Run the Flask Server
bash
Copy code
python app.py
View the App in Browser
arduino
Copy code
http://localhost:5000
📷 Screenshots
🏠 Home Page
(Insert your flowchart and UI screenshot here)

📋 Diagnosis Page
(Insert diagnosis screenshot here)

🧠 How the AI Logic Works
Each disease has:

Required Symptoms

Optional Symptoms

Rule Conditions

Recommendation

Confidence Score:

mathematica
Copy code
Score = (Required Matched / Required Total) 
      + 0.5 × (Optional Matched / Optional Total)
📌 Future Improvements
Add more diseases like Dengue, Viral Fever, COVID

Add doctor login panel

Add PDF report export

Add database storage (MySQL / MongoDB)

Machine learning enhancement

🤝 Contributing
Pull requests are welcome!
For major changes, open an issue first.

📄 License
This project is created for educational purposes.


✔ A longer README
✔ A professional GitHub cover image
✔ A badge section (Python, Flask, MIT license, stars, forks)
