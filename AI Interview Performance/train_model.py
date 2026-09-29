import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load dataset
df = pd.read_csv("dataset/interview_dataset.csv")

# Input and Output
X = df["Answer"]
y = df["Score"]

# Convert text into numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained successfully!")