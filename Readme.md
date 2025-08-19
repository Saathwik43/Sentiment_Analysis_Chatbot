# Sentiment Analysis Chatbot

## 🎯 Project Overview
A beginner-friendly GUI-based sentiment analysis chatbot that analyzes text sentiment using natural language processing. This project is perfect for learning NLP basics and GUI development.

## 🌟 Real-World Applications
- **Customer Feedback Analysis**: Analyze customer reviews and feedback automatically
- **Social Media Monitoring**: Monitor sentiment of social media mentions
- **Business Intelligence**: Understand customer sentiment trends
- **Content Moderation**: Identify potentially negative content
- **Market Research**: Analyze survey responses and comments

## 🚀 Features
- **Easy-to-Use GUI**: Clean and intuitive interface built with Tkinter
- **Real-Time Analysis**: Instant sentiment analysis of any text input
- **Detailed Reports**: Comprehensive analysis including polarity, subjectivity, and business insights
- **History Tracking**: Save and visualize analysis history
- **Visual Charts**: View sentiment trends over time
- **Export Capability**: Save analysis history to JSON format

## 📋 Requirements
- Python 3.7 or higher
- See `requirements.txt` for package dependencies

## 🔧 Installation & Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt

# Download NLTK data (required for TextBlob)
python -c "import nltk; nltk.download('punkt'); nltk.download('brown')"
```

### Step 2: Run the Application
```bash
python sentiment_chatbot.py
```

## 📖 How to Use

1. **Launch the Application**: Run the Python script
2. **Enter Text**: Type or paste text into the input area
3. **Analyze**: Click "🔍 Analyze Sentiment" button
4. **View Results**: Read the detailed analysis report
5. **Track History**: Click "📈 View History" to see sentiment trends
6. **Clear**: Use "🗑️ Clear" to reset for new analysis

## 🧠 Understanding the Results

### Polarity Score (-1 to +1)
- **Positive (0.1 to 1.0)**: Happy, satisfied, approving sentiment
- **Neutral (-0.1 to 0.1)**: Balanced or factual content
- **Negative (-1.0 to -0.1)**: Unhappy, critical, disapproving sentiment

### Subjectivity Score (0 to 1)
- **Objective (0.0 to 0.4)**: Factual, informational content
- **Subjective (0.4 to 1.0)**: Opinion-based, emotional content

## 💼 Resume Value
This project demonstrates:
- **Python Programming**: Clean, well-structured code
- **GUI Development**: Tkinter interface design
- **Natural Language Processing**: TextBlob and NLTK usage
- **Data Visualization**: Matplotlib integration
- **File Handling**: JSON data persistence
- **Error Handling**: Robust exception management
- **User Experience**: Intuitive interface design

## 🎓 Learning Outcomes
- Understand sentiment analysis fundamentals
- Learn GUI development with Tkinter
- Practice data visualization with Matplotlib
- Implement file I/O operations
- Handle real-world NLP challenges
- Create user-friendly applications

## 🔧 Technical Skills Gained
- Python programming
- Natural Language Processing (NLP)
- GUI development
- Data visualization
- JSON file handling
- Object-oriented programming
- Error handling and validation

## 📈 Potential Enhancements
- Add more advanced NLP models (VADER, BERT)
- Implement batch file processing
- Add export to CSV/Excel functionality
- Include emoji sentiment analysis
- Add multi-language support
- Implement API integration for real-time data

---
