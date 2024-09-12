# NLPApp-
The NLP Sentiment Analysis App is a Python-based graphical application that allows users to analyze the sentiment of a text input. Developed using tkinter for the user interface and nltk (Natural Language Toolkit) for sentiment analysis, the app offers a smooth and user-friendly experience.

Features
User Authentication: Users can create an account and log in securely using an SQLite database for managing credentials.
Sentiment Analysis: The app uses NLTK's VADER sentiment analysis to return scores for positive, negative, neutral, and compound sentiments based on the text input.
Simple and Intuitive GUI: A clean, responsive interface built with tkinter, allowing users to easily navigate between login, signup, and analysis pages

Technology Stack
Frontend: Python tkinter for the graphical user interface.
Backend:
NLTK: Natural Language Toolkit for sentiment analysis (VADER).
SQLite: Database for user authentication.

Installation Instructions
1. Clone the Repository:
2. git clone https://github.com/AyaanShaheer/NLP-App.git
cd NLP-App

Install Dependencies
Install the necessary Python packages using pip:
pip install nltk
pip install tk


Download NLTK's VADER lexicon:
import nltk
nltk.download('vader_lexicon')


 Run the App
Once dependencies are installed, you can run the app with:
python nlp_app.py

Usage
Sign Up: First-time users can sign up with a username and password.
Log In: Returning users can log in using their credentials.
Analyze Text: Once logged in, users can input any paragraph, and the app will analyze the sentiment, displaying the positive, neutral, negative, and overall sentiment results.

Future Enhancements
Add password encryption for better security.
Expand sentiment analysis to support multiple languages.
Improve the user interface with additional themes and design elements.


Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

