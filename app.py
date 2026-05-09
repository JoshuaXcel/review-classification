import streamlit as st
import joblib

model = joblib.load("customer_review_model.pkl")
vectorizer = joblib.load("text_vectorizer.pkl")

st.title("🛍️ Customer Review Classifier")
st.write("Type a review below and find out if it's **Positive** or **Negative**.")

review = st.text_area("Enter your review here:")

if st.button("Classify"):
    if review.strip() == "":
        st.warning("Please enter a review first.")
    else:
        features = vectorizer.transform([review])
        prediction = model.predict(features)[0]
        confidence = model.predict_proba(features)[0]

        if prediction == 1:
            st.success(f"✅ Positive Review  with  {round(confidence[1] * 100, 1)}% confidence")
        else:
            st.error(f"❌ Negative Review  with  {round(confidence[0] * 100, 1)}% confidence")
