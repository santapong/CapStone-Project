from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# Updated dataset with more examples
data = {
    "text": [
        "PLC programming and SCADA systems are core to factory automation.",
        "IoT enables smart factories and predictive maintenance.",
        "PID controllers are essential for process control.",
        "Robotics and machine vision optimize production lines.",
        "Industrial IoT helps integrate sensors with cloud platforms.",
        "Safety protocols like ISA standards are crucial in automation.",
        "Predictive maintenance reduces unplanned downtime.",
        "SCADA systems monitor industrial processes efficiently.",
        "IoT provides insights from industrial sensors.",
        "PID controllers stabilize industrial processes.",
        "ISA safety standards guide automation implementations.",
    ],
    "category": [
        "Factory Automation",
        "IoT",
        "Process Control",
        "Factory Automation",
        "IoT",
        "Safety and Standards",
        "IoT",
        "Process Control",
        "IoT",
        "Process Control",
        "Safety and Standards",
    ]
}

# Convert to a DataFrame
df = pd.DataFrame(data)

# Features and labels
X = df['text']
y = df['category']

# Stratified train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=4, random_state=42, stratify=y
)

# TF-IDF transformation
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train the model
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# Predict on test set
y_pred = model.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Example new samples
new_texts = [
    "Smart factories leverage IoT for real-time monitoring.",
    "SCADA systems are used in process control.",
    "Robotic arms are essential in modern production lines."
]

# Transform new text data using the fitted vectorizer
new_texts_tfidf = vectorizer.transform(new_texts)

# Predict the categories
predictions = model.predict(new_texts_tfidf)
for text, category in zip(new_texts, predictions):
    print(f"Text: '{text}' => Predicted Category: {category}")