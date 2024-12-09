<h1>Spam Email Classifier</h1>
This project is a Spam Email Classifier built using machine learning techniques. It uses an SVM (Support Vector Machine) model trained on a labeled dataset of spam and non-spam (ham) emails. The classifier can predict whether an email is spam or not.

<h2>Features</h2>
Preprocessing pipeline to clean and transform text data.
Uses TF-IDF Vectorization for feature extraction.
Hyperparameter tuning using GridSearchCV.
SVM-based model for spam detection.
Custom email prediction function.

<h2>Dataset</h2>
The dataset used for this project contains labeled email data with two classes:

Spam: Emails flagged as unwanted or malicious.
Ham: Normal, non-spam emails.
The dataset is expected to have the following columns:

text: The email content.
label: The label (e.g., "ham" or "spam").
label_num: Numerical representation of the label (0 for ham, 1 for spam).
