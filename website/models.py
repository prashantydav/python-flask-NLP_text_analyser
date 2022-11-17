from mongoengine import *

connect(host = "mongodb://root:password@172.17.0.1.2:27017/NLP_db")

class Text(Document):
    id = IntField(max_value = 5000)
    text = StringField(required = True)
    length = IntField(max_value = 1000)
    pos_analysis = DictField()
    sentiment_analysis = StringField(max_length = 8)
    ner_analysis = DictField()


# number of times webapp was used.
# Number of sentences that are stored in the database.
# number of different Positive and Negitive sentences.
# what is the average length of the sentences that the user input.