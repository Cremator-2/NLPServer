import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup


class TextPreprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stemmer = PorterStemmer()

    @staticmethod
    def remove_html_tags(text):
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()

    @staticmethod
    def to_lowercase( text):
        return text.lower()

    @staticmethod
    def remove_urls(text):
        return re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)

    @staticmethod
    def remove_punctuation(text):
        return re.sub(r'[^\w\s]', '', text)

    def remove_stop_words(self, text):
        text_tokens = nltk.word_tokenize(text)
        filtered_text = [word for word in text_tokens if word not in self.stop_words]
        return ' '.join(filtered_text)

    def stem_text(self, text):
        text_tokens = nltk.word_tokenize(text)
        stemmed_text = [self.stemmer.stem(word) for word in text_tokens]
        return ' '.join(stemmed_text)

    def preprocess(self, text):
        text = self.remove_html_tags(text)
        text = self.to_lowercase(text)
        text = self.remove_urls(text)
        text = self.remove_punctuation(text)
        text = self.remove_stop_words(text)
        text = self.stem_text(text)
        return text
