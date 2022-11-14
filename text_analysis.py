import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from spacy import displacy
import spacy
from spacy import tokenizer



stop_words = set(stopwords.words('english'))

txt = "Pythons design philosophy emphasizes code readability with"

def pos_analysis(txt):
    tokenized  = sent_tokenize(txt)
    corpus = []
    for i in tokenized:
        wordlist = nltk.word_tokenize(i)
        wordlist = [w for w in wordlist if not w in stop_words]
        tagged = nltk.pos_tag(wordlist)
        corpus.append(tagged)

    return corpus

def sentiment_analysis(txt):

    sia = SentimentIntensityAnalyzer()
    
    tup = sia.polarity_scores(txt)
    pos = tup['pos']
    neg = tup['neg']
    neu = tup['neu']
    
    res = ""
    if pos>neg:
        res = "pos" if pos>neu else "neu"
    else:
        res = "neg" if neg>neu else "neu"

    return res

def ner_analysis(txt):
    train_text = state_union.raw()
    sample_text = state_union.raw('2006-GWBush.txt')

    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    tokenized = custom_sent_tokenizer.tokenize(txt)

    for i in tokenized:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        namedEnt = nltk.ne_chunk(tagged, binary=False)
        print(namedEnt)
        namedEnt.draw()
    # nlp = spacy.load('en_core_web_sm')
    # doc = nlp(txt)
    
    # ents = [(e.text , e.label_) for e in doc.ents]
    # return ents

print(pos_analysis(txt))
print(ner_analysis(txt))