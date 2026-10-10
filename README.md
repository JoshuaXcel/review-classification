# 🛍️ Customer Review Classifier

![Python](https://img.shields.io/badge/Python-1E3A8A?logo=python&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-2563EB?logo=scikitlearn&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-1E40AF?logo=streamlit&logoColor=white) ![NLP](https://img.shields.io/badge/NLP-1D4ED8?logo=python&logoColor=white)

A Streamlit app that reads a customer review and tells you whether it is **Positive** or **Negative**, along with the model's confidence.

## What it does

1. Type or paste a review into the text box
2. Click **Classify**
3. The app shows ✅ *Positive Review* or ❌ *Negative Review*, with the predicted class probability as a percentage

Empty input is caught with a friendly warning.

## Approach / model

This is a classic text-classification pipeline:

- **Text features:** scikit-learn `TfidfVectorizer` turns the review into TF-IDF features (saved as `text_vectorizer.pkl`)
- **Classifier:** scikit-learn `LogisticRegression` predicts the sentiment, where 1 = positive and 0 = negative (saved as `customer_review_model.pkl`)
- **Confidence:** comes from `predict_proba`

## Dataset

The training dataset and training notebook are not included in this repository. Only the trained vectorizer and model are committed.

## How to run

```bash
git clone https://github.com/JoshuaXcel/review-classification.git
cd review-classification
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Project structure

```
app.py                     Streamlit app
customer_review_model.pkl  Trained Logistic Regression classifier
text_vectorizer.pkl        Fitted TF-IDF vectorizer
requirements.txt           Python dependencies
```

## Tech used

Python · scikit-learn (TF-IDF, Logistic Regression) · Streamlit · joblib

## Author

**Joshua Mudana (Excel)**, AI & Machine Learning Engineer

[Portfolio](https://joshuaxcel.github.io/joshuamudana-portfolio/) · [GitHub](https://github.com/JoshuaXcel) · [X](https://x.com/JoshuaXcell) · mudanajoshua@gmail.com
