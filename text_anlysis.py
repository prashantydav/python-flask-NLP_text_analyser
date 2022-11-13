import nltk
nltk.download('stopwords')
nltk.download('word_tokenize')
nltk.download('sent_tokenize')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize , sent_tokenize
stop_words = set(stopwords.words('english'))

test_txt = "You are a fucked up person"

def POS_analysis(txt):
    tokenized  = sent_tokenize(txt)
    corpus = []
    for i in tokenized:
        wordlist = nltk.word_tokenize(i)
        wordlist = [w for w in wordlist if not w in stop_words]
        tagged = nltk.pos_tag(wordlist)
        corpus.append(tagged)

    return corpus


        