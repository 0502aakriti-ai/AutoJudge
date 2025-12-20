import streamlit as st
import pickle

# Load saved models
with open("tfidf.pkl", "rb") as f:
    tfidf = pickle.load(f)

with open("clf_model.pkl", "rb") as f:
    clf = pickle.load(f)

with open("reg_model.pkl", "rb") as f:
    reg = pickle.load(f)

st.set_page_config(page_title="Problem Difficulty Predictor", layout="centered")
st.markdown("""
<style>
.main {
    background-color: #f7f9fc;
}
.result-box {
    padding: 20px;
    border-radius: 10px;
    background-color: #ffffff;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.05);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧠 Programming Problem Difficulty Predictor")
st.subheader("Predict problem complexity using Machine Learning")
st.write(
    "Paste the **problem statement**, **input**, and **output description** below "
    "to get the predicted difficulty level and score."
)


st.markdown("### ✍️ Enter Problem Details")

description = st.text_area(
    "📘 Problem Description",
    height=150,
    placeholder="Describe the problem statement here..."
)

input_desc = st.text_area(
    "📥 Input Description",
    height=100,
    placeholder="Describe the input format..."
)

output_desc = st.text_area(
    "📤 Output Description",
    height=100,
    placeholder="Describe the output format..."
)


if st.button("🚀 Predict Difficulty"):
    combined_text = description + " " + input_desc + " " + output_desc

    if combined_text.strip() == "":
        st.warning("⚠️ Please fill in at least one field before predicting.")
    else:
        text_vec = tfidf.transform([combined_text])

        pred_class = clf.predict(text_vec)[0]
        pred_score = reg.predict(text_vec)[0]



        st.success(f"🧩 Predicted Difficulty Class: **{pred_class}**")
        st.info(f"📊 Predicted Difficulty Score: **{pred_score:.2f}**")
