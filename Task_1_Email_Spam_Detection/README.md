# Email Spam Detection using Machine Learning

## Objective
To build a machine learning model that classifies emails as **Spam** or **Ham** using Natural Language Processing techniques.

## Dataset
- Source: Kaggle
- Contains labeled email messages as spam or ham

## Workflow
1. Data cleaning and exploratory data analysis
2. Text preprocessing (lowercasing, tokenization, stopword removal, stemming)
3. Feature extraction using TF-IDF
4. Model training using Multinomial Naive Bayes
5. Model evaluation using precision, recall, confusion matrix
6. Deployment using Streamlit

## Model Choice
TF-IDF was selected over CountVectorizer to prioritize **precision**, minimizing false positives where legitimate emails are incorrectly classified as spam.

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- NLTK
- Streamlit

## How to Run the App
```
pip install streamlit
streamlit run app.py

```