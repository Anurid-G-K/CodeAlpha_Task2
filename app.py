from flask import Flask, render_template, request, jsonify
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
with open("data/faq_data.json", "r") as f:
    data = json.load(f)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# Vectorize questions
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-answer", methods=["POST"])
def get_answer():
    user_question = request.json["question"]
    user_vector = vectorizer.transform([user_question])
    similarity_scores = cosine_similarity(user_vector, question_vectors)
    best_match_index = similarity_scores.argmax()
    best_answer = answers[best_match_index]
    return jsonify({"answer": best_answer})

if __name__ == "__main__":
    app.run(debug=True)
