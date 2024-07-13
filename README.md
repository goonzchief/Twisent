# Twisent
Twisent is a Python application that performs real-time sentiment analysis on live tweets using the Twitter API, natural language processing (NLP), and machine learning techniques. The program fetches live tweets, preprocesses the text, analyzes the sentiment using both VADER and TextBlob, and displays the results in a live-updating graph.


Features
Real-time sentiment analysis of live tweets
Dual sentiment analysis using VADER and TextBlob
Advanced text preprocessing
Live-updating graph of sentiment scores
Data persistence with CSV export
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Twisent.git
cd Twisent
Create and activate a virtual environment:

bash
Copy code
python -m venv env
source env/bin/activate   # On Windows use `env\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Download NLTK VADER lexicon:

bash
Copy code
python -c "import nltk; nltk.download('vader_lexicon')"
Usage
Replace the placeholder strings in the script with your actual Twitter API credentials:

python
Copy code
api_key = 'YOUR_API_KEY'
api_key_secret = 'YOUR_API_KEY_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
Run the script:

bash
Copy code
python twisent.py
The live graph displaying sentiment analysis will appear, and the tweet data along with sentiment scores will be saved to tweet_sentiments.csv.

Requirements
tweepy
textblob
matplotlib
pandas
nltk
You can install these packages using:

bash
Copy code
pip install tweepy textblob matplotlib pandas nltk
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.
