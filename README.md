<h1>Spam Email Classification using NLP & ML</h1>
This project demonstrates how to build a Spam Email Classifier using Natural Language Processing (NLP) and Machine Learning techniques. The classifier processes email text, extracts features using TF-IDF Vectorization, and trains an SVM (Support Vector Machine) to distinguish between spam and non-spam (ham) emails.

<h2>Features</h2>
Preprocessing pipeline to clean and normalize email text (removes punctuation, stopwords, and applies stemming).
TF-IDF Vectorization for text feature extraction.
Hyperparameter tuning with GridSearchCV for optimal model performance.
Visualization of class distribution and evaluation metrics like confusion matrix.
Supports predictions on new email samples.

<h2>Dataset</h2>
The dataset used for this project contains labeled email data with two classes:

Spam: Emails flagged as unwanted or malicious.
Ham: Normal, non-spam emails.
The dataset is expected to have the following columns:

text: The email content.
label: The label (e.g., "ham" or "spam").
label_num: Numerical representation of the label (0 for ham, 1 for spam).
