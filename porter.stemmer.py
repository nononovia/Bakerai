import string
import nltk 
from nltk.stem import PorterStemmer
from process_data import allWords

ps = PorterStemmer()

pd.set_option('display.max_colwidth', 100)
stopwords = nltk.corpus.stopwords.word('english')

def clean_text(text):

