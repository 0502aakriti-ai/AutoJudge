# 🧠 Programming Problem Difficulty Predictor

This project builds an end-to-end machine learning system to predict the
difficulty level of programming problems based solely on their textual
descriptions.

The system predicts:
- **Difficulty Class**: Easy / Medium / Hard (Classification)
- **Difficulty Score**: Numerical value representing problem complexity (Regression)

A simple web interface is provided using **Streamlit**.

---

## 📂 Dataset

The dataset used in this project contains programming problems annotated with
difficulty class and numerical difficulty score.

Each data sample includes:
- Problem title
- Problem description
- Input description
- Output description
- Difficulty class (Easy / Medium / Hard)
- Difficulty score (numerical)

The dataset is provided in **JSONL format** and can be accessed here:

🔗 Dataset link:  
https://raw.githubusercontent.com/AREEG94FAHAD/TaskComplexityEval-24/main/problems_data.jsonl

> Note: The dataset is not uploaded to this repository due to size constraints
and is accessed directly from the source.


---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression (Classification)
- Linear Regression (Regression)
- Streamlit (Web Interface)

---

## 🧠 Approach

1. Combined problem description, input, and output text into a single feature.
2. Converted text into numerical vectors using **TF-IDF**.
3. Trained two independent models:
   - Classification model to predict difficulty class
   - Regression model to predict difficulty score
4. Evaluated models using:
   - Accuracy and Confusion Matrix (Classification)
   - MAE and RMSE (Regression)
5. Built a Streamlit web app for real-time predictions.

---

## 🌐 Web Application

The Streamlit interface allows users to:
1. Enter a programming problem description
2. Click "Predict Difficulty"
3. View predicted difficulty class and score

To run the app locally:

```bash
streamlit run app.py
```

---
## 📦 Installation

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📊 Results

The model successfully predicts problem difficulty using only textual features.

Minor inconsistencies between class and score predictions may occur due to
independent model optimization and dataset noise.

---

## 👩‍💻 Author

Aakriti
Undergraduate Student, IIT Roorkee
