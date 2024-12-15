import streamlit as st
import pickle

# Load the pre-trained model and vectorizer
with open('svm_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def clean_text(text):
    """Utility function for preprocessing the email text."""
    import string
    from nltk.corpus import stopwords
    from nltk.stem import SnowballStemmer
    import nltk

    nltk.download('stopwords', quiet=True)
    stop_words = stopwords.words('english')
    stemmer = SnowballStemmer('english')

    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    # Remove stopwords and apply stemming
    words = text.split()
    words = [stemmer.stem(word) for word in words if word.lower() not in stop_words]
    return ' '.join(words)

def predict_email(email):
    """Predict if the email is Spam or Ham."""
    cleaned_email = clean_text(email)
    vectorized_email = vectorizer.transform([cleaned_email])
    prediction = model.predict(vectorized_email)
    return "Ham" if prediction[0] == 0 else "Spam"

# Streamlit app interface
st.title("📧 Spam Email Detection")
st.write("Enter the email content below to predict whether it is Spam or Ham:")

# Input email content
email_content = st.text_area("Email Content")

# Predict button
if st.button("Predict"):
    if email_content.strip() == "":
        st.warning("Please enter some email content.")
    else:
        result = predict_email(email_content)
        st.success(f"The email is predicted as: **{result}**")
