# Email Spam Detection using Machine Learning
**OIBSIP – Task 1**

## 📌 Objective
This project focuses on building a **text classification pipeline** using **TF-IDF vectorization** and traditional **machine learning models**.  
The primary goal is to prioritize **precision over recall**, making TF-IDF a better choice than CountVectorizer for this task.

The project was developed as part of the **OIBSIP Internship Program**, and this repository will eventually contain **three tasks**, uploaded incrementally.

## 📂 Dataset
- Source: Kaggle
- Contains labeled email messages as spam or ham

## ⚙️ Workflow
1. Data cleaning and exploratory data analysis
2. Text preprocessing (lowercasing, special character removal, tokenization, stopword removal, stemming)
3. Feature extraction using TF-IDF Vectorizer
4. Model training using Multinomial Naive Bayes
5. Model evaluation using precision, recall, F!-score and confusion matrix

## 🧠 Model Choice
TF-IDF (Term Frequency–Inverse Document Frequency) was chosen over CountVectorizer because:

- It **down-weights common but uninformative words**
- It emphasizes **discriminative terms**
- It generally improves **precision**, which is critical for this task, minimizing false positives where legitimate emails are incorrectly classified as spam.

## 🛠️ Tech Stack
- Python
- Pandas
- Matplotlib / Seaborn
- Scikit-learn
- NLTK
- Jupyter Notebook

## 🙌 Acknowledgements
This project was completed as part of the **OIBSIP Internship Program**, with a focus on practical machine learning workflows and reproducible research.