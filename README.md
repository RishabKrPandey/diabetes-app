# 🩺 Diabetes Prediction App  

A simple **FastAPI + Machine Learning** web app that predicts whether a patient is likely to have diabetes based on health parameters.  

This project uses a trained **scikit-learn model** with preprocessing and serves predictions through a user-friendly web interface.  

---

## 🚀 Features
- Predicts **Diabetes / Not Diabetic** based on input health details.  
- Built with **FastAPI** for backend & **Jinja2 + Bootstrap** for frontend.  
- Interactive web form with user-friendly field descriptions.   

---

## 📊 Input Fields
- **Pregnancies** – Number of pregnancies  
- **Glucose** – Plasma glucose concentration  
- **Blood Pressure** – Diastolic blood pressure (mm Hg)  
- **Skin Thickness** – Triceps skinfold thickness (mm)  
- **Insulin** – 2-Hour serum insulin (mu U/ml)  
- **BMI** – Body Mass Index (kg/m²)  
- **Diabetes Pedigree Function** – Family history influence score  
- **Age** – Patient age  

---

## 🛠️ Tech Stack
- **FastAPI** – Web framework  
- **Scikit-learn** – ML model(RandomForest)
- **Pandas & NumPy** – Data processing  
- **Bootstrap** – UI styling  
- **Jinja2** – Template rendering  

---

## ⚡ Installation & Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/diabetes-app.git
   cd diabetes-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   uvicorn main:app --reload
   ```
5. Open in browser:
   ```bash
   http://127.0.0.1:8000
   ```

## 📸 Screenshot
<img width="1914" height="993" alt="image" src="https://github.com/user-attachments/assets/5d664ef1-146f-4c4f-b947-3dcb37683e3f" />

<img width="1892" height="991" alt="image" src="https://github.com/user-attachments/assets/a05f4f38-62be-48ea-8c3d-7428f52d94e6" />



