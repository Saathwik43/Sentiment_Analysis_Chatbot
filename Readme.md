# 🤖 Sentiment Analysis Chatbot

## 🎯 Project Overview

A beginner-friendly **Streamlit-based** sentiment analysis chatbot that analyzes text sentiment using natural language processing. This project is perfect for learning NLP basics, interactive dashboard development, and data visualization.

##live demo : https://sentimentanalysischatbot.streamlit.app/

## 🌟 Real-World Applications

* **Customer Feedback Analysis**: Automatically analyze customer reviews and feedback.
* **Social Media Monitoring**: Track sentiment of mentions on social media.
* **Business Intelligence**: Understand customer sentiment trends.
* **Content Moderation**: Detect potentially negative or harmful content.
* **Market Research**: Analyze survey responses and open-ended comments.

## 🚀 Features

* **Interactive Web App**: Built with Streamlit for a modern, user-friendly interface.
* **Real-Time Analysis**: Instantly analyze sentiment of any text input.
* **Detailed Reports**: Includes polarity, subjectivity, interpretations, and business insights.
* **History Tracking**: Save, review, and visualize past analyses.
* **Visual Charts**: Polarity/subjectivity charts and history trends.
* **Sample Texts**: Quickly test the app with pre-loaded examples.

## 📋 Requirements

* Python 3.8 or higher
* See `requirements.txt` for dependencies

## 🔧 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <your-repo-link>
cd <your-repo-folder>
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt

# Download NLTK data (required for TextBlob)
python -c "import nltk; nltk.download('punkt'); nltk.download('brown')"
```

### Step 3: Run the Application

```bash
streamlit run app.py
```

## 📖 How to Use

1. **Launch the App**: Run `streamlit run app.py`
2. **Enter Text**: Type or paste text into the input area.
3. **Analyze**: Click "🔍 Analyze Sentiment" to get results.
4. **View Results**: See polarity, subjectivity, interpretations, and insights.
5. **Track History**: Open the sidebar and click "📈 View History".
6. **Clear History**: Use "🗑️ Clear History" to reset past analyses.

## 🧠 Understanding the Results

### Polarity Score (-1 to +1)

* **Positive (0.1 to 1.0)** → Happy, satisfied, approving sentiment.
* **Neutral (-0.1 to 0.1)** → Balanced or factual.
* **Negative (-1.0 to -0.1)** → Unhappy, critical, disapproving sentiment.

### Subjectivity Score (0 to 1)

* **Objective (0.0 to 0.4)** → Mostly factual.
* **Moderately Subjective (0.4 to 0.7)** → Mix of facts and opinions.
* **Highly Subjective (0.7 to 1.0)** → Emotion-driven, opinion-based.

## 💼 Resume Value

This project demonstrates:

* **Python Programming** (clean, structured OOP-based code)
* **Streamlit App Development** (interactive dashboards)
* **Natural Language Processing** (TextBlob, NLTK)
* **Data Visualization** (Matplotlib, Streamlit charts)
* **File Handling** (JSON persistence)
* **Error Handling** (robust exception management)
* **User Experience** (clear layout, instructions, and sample data)

## 🎓 Learning Outcomes

* Understand sentiment analysis fundamentals.
* Build an interactive NLP dashboard with Streamlit.
* Practice data visualization with Matplotlib.
* Implement file I/O operations for saving history.
* Handle real-world NLP challenges.
* Create a user-friendly application.

## 🔧 Technical Skills Gained

* Python Programming
* Natural Language Processing (NLP)
* Streamlit Web App Development
* Data Visualization
* JSON File Handling
* Object-Oriented Programming
* Error Handling & Validation

## 📈 Potential Enhancements

* Add advanced NLP models (VADER, BERT, Hugging Face Transformers).
* Implement batch file/text processing.
* Export analysis to CSV/Excel.
* Include emoji sentiment analysis.
* Add multi-language support.
* Integrate real-time API data (e.g., Twitter sentiment).

---
