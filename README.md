# CodeAlpha_Task2


# ♟️ Chess FAQ Chatbot

A simple yet powerful FAQ chatbot built with Python and Flask to answer user queries related to the game of chess. The bot uses cosine similarity to find the best matching answer from a dataset of 400+ frequently asked questions.

---

## 📌 Features

- 🔍 Intelligent question matching using cosine similarity.
- 📚 400+ curated chess-related Q&A pairs.
- 🖥️ Simple, clean web interface built with HTML + CSS.
- 🚀 Lightweight and easy to deploy.
- 🧠 Expandable: Add more questions or switch domains easily.


## 📂 Project Structure
chess-faq-chatbot/
├── static/
│ └── style.css # Frontend styling
├── templates/
│ └── index.html # Frontend UI
├── chatbot.py # Main Flask server
├── faq_dataset.json # Q&A data (400+ chess-related FAQs)
├── requirements.txt 
└── README.md 



## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chess-faq-chatbot.git
cd chess-faq-chatbot

2. Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Bot Locally
python chatbot.py



🛠 Technologies Used
Python 3
Flask
scikit-learn
NumPy
HTML/CSS (for frontend)


Future Improvements
Add NLP models like BERT or sentence transformers
Add speech-to-text and text-to-speech capabilities
Deploy on platforms like Render, Vercel, or Heroku
Convert into a Telegram or WhatsApp bot
