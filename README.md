# Twisent

Twisent is a Python application that performs real-time sentiment analysis on live tweets using the Twitter API, natural language processing (NLP), and machine learning techniques. The program fetches live tweets, preprocesses the text, analyzes the sentiment using both VADER and TextBlob, and displays the results in a live-updating graph.

## Features

- Real-time sentiment analysis of live tweets
- Dual sentiment analysis using VADER and TextBlob
- Advanced text preprocessing
- Live-updating graph of sentiment scores
- Data persistence with CSV export

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/goonzchief/Twisent.git
    cd Twisent
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate   # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Download NLTK VADER lexicon:

    ```bash
    python -c "import nltk; nltk.download('vader_lexicon')"
    ```
    ## Requirements

- tweepy
- textblob
- matplotlib
- pandas
- nltk

You can install these packages using:

```bash
pip install tweepy textblob matplotlib pandas nltk
```

## Usage

1. Replace the placeholder strings in the script with your actual Twitter API credentials:

    ```python
    api_key = 'YOUR_API_KEY'
    api_key_secret = 'YOUR_API_KEY_SECRET'
    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'
    ```

2. Run the script:

    ```bash
    python twisent.py
    ```

3. The live graph displaying sentiment analysis will appear, and the tweet data along with sentiment scores will be saved to `tweet_sentiments.csv`.



## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
