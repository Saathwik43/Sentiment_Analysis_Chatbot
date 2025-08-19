Sentiment Analyzer Chatbot
Project Description
This project is a Sentiment Analysis Chatbot built using Streamlit. It's designed to help users quickly and easily analyze the sentiment of any text input, determining its polarity (positive, negative, or neutral) and subjectivity (factual vs. opinion-based). The application provides detailed analytical results, actionable business insights, and interactive visualizations, along with a historical record of all analyses.

Features
Real-time Sentiment Analysis: Instantly analyze the emotional tone of text.

Polarity and Subjectivity Scores: Get quantitative metrics for sentiment and the degree of personal opinion.

Detailed Breakdown: Access comprehensive statistics like word count, character count, and an estimated sentence count, alongside a descriptive interpretation of sentiment strength and subjectivity type.

Actionable Business Insights: Receive practical recommendations based on the analysis, such as identifying content suitable for testimonials or feedback requiring immediate attention.

Interactive Visualizations: Visualize polarity and subjectivity scores with bar charts and see the overall sentiment distribution of your analysis history with a pie chart.

Analysis History: The application automatically saves your last 50 analyses to a local file, allowing for easy review and trend tracking.

Dashboard: A convenient sidebar dashboard provides quick access to view and clear your analysis history.

Sample Text Functionality: Test the application effortlessly using pre-defined sample texts to see its capabilities.

How to Run
To get this Sentiment Analysis Chatbot up and running on your local machine, follow these steps:

Clone the Repository:
First, clone the project repository to your local system using Git:

git clone [your_repository_url]
cd [your_repository_name] # Replace with your project directory name


Install Dependencies:
This project relies on several Python libraries. It's highly recommended to create and activate a virtual environment before installing them to avoid conflicts with other projects.

# Create a virtual environment (optional but recommended)
python -m venv venv
# Activate the virtual environment
# On Windows:
# .\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install the required libraries
pip install streamlit textblob pandas matplotlib numpy


Download TextBlob Corpora:
The TextBlob library needs specific linguistic data to perform sentiment analysis. You'll need to download these corpora:

python -m textblob.download_corpora


Run the Streamlit Application:
Once all dependencies are installed and the corpora are downloaded, navigate to the project's root directory in your terminal and execute:

streamlit run [your_main_app_file_name].py # Replace with the actual name of your Python file (e.g., app.py or main.py)


This command will launch the Streamlit application, and it should automatically open in your default web browser.

File Structure
[your_main_app_file_name].py: This is the primary Python script that contains all the code for the Streamlit application.

sentiment_history.json: This JSON file is automatically created and used by the application to store a record of your sentiment analysis history.

Technology Stack
Python: The foundational programming language for the entire application.

Streamlit: Utilized for rapid development and deployment of interactive web applications, providing the user interface.

TextBlob: A powerful Python library specifically chosen for its efficient and straightforward sentiment analysis capabilities.

Pandas: Employed for data manipulation and analysis, particularly for structuring and displaying the analysis history.

Matplotlib: Used for creating static, interactive, and animated visualizations, including the sentiment charts.

NumPy: Provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays, used for numerical computations within the analysis.

JSON: Used for data serialization and deserialization, enabling the persistence of analysis history.
