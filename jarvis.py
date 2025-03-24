import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import os
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


def main():
    while True:
        user_input = input("\nEnter a sentence: ")
        if user_input == "exit":
            print("Goodbye!")
            break
        result=sia.polarity_scores(user_input)
        print(result)

if __name__ == "__main__":
    main()