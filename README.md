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

## 📊 Evaluation Metrics

The performance of the models was evaluated using standard machine learning metrics.

### 🔹 Classification (Difficulty Class Prediction)
- **Accuracy**: Measures the proportion of correctly predicted difficulty classes (Easy / Medium / Hard).
- A confusion matrix was also used to analyze class-wise prediction performance.
- <img width="706" height="591" alt="Screenshot 2026-01-03 221507" src="https://github.com/user-attachments/assets/da960245-b2a0-43a5-995a-39cf5c2d4821" />


### 🔹 Regression (Difficulty Score Prediction)
- **Mean Absolute Error (MAE)**: Measures the average absolute difference between predicted and actual difficulty scores.
- **Root Mean Squared Error (RMSE)**: Penalizes larger prediction errors and provides insight into prediction variance.
- <img width="635" height="173" alt="Screenshot 2026-01-03 221526" src="https://github.com/user-attachments/assets/157edbcd-a8b1-475c-b41f-310d92e7c96d" />


These metrics help assess both the correctness of difficulty classification and the reliability of numerical difficulty score prediction.

---

## 📌 Model Performance Summary

| Task | Metric | Value |
|----|------|------|
| Classification | Accuracy | 0.50789 |
| Regression | MAE | 3.69918 |
| Regression | RMSE | 4.70622 |



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

## 📽️Demo VIdeo
The link for the demo video of the project is as follows:

https://drive.google.com/file/d/1Wszvi0xSVsOW5gYlfA7G45LLaA3tYMh2/view?usp=sharing

---


## 📊 Results

The model successfully predicts problem difficulty using only textual features.

Minor inconsistencies between class and score predictions may occur due to
independent model optimization and dataset noise.

---

## 👩‍💻 Author

Aakriti
Undergraduate Student, IIT Roorkee
