import joblib

# Load model and vectorizer
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Take input
answer = input("Enter your interview answer: ")

# Convert text into numbers
answer_vector = vectorizer.transform([answer])

# Predict score
score = model.predict(answer_vector)

print("Predicted Interview Score:", round(score[0], 2))