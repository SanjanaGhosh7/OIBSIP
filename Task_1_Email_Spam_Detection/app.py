import os
import streamlit as st
import pickle
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to saved artifacts
model_path = os.path.join(BASE_DIR, "model.pkl")
tfidf_path = os.path.join(BASE_DIR, "tfidf.pkl")

# Load saved model and vectorizer
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(tfidf_path, "rb") as f:
    tfidf = pickle.load(f)

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Initialize stemmer and stopwords
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Function to preprocess text

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()

def preprocess_text(text):
    # 1. Lowercasing
    text = text.lower()

    # 2. Remove special characters
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # 3. Tokenization
    tokens = nltk.word_tokenize(text)

    # 4. Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # 5. Stemming
    tokens = [ps.stem(word) for word in tokens]


    return " ".join(tokens)

# App UI
st.title("📧 Email Spam Detection App")
st.write("Enter an email message below to check whether it is **Spam** or **Ham**.")

user_input = st.text_area("Enter email text here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        processed_text = preprocess_text(user_input)
        vectorized_text = tfidf.transform([processed_text])
        prediction = model.predict(vectorized_text)[0]

        if prediction == 1:
            st.error("🚨 This email is **SPAM**")
        else:
            st.success("✅ This email is **HAM (Not Spam)**")