from flask import Blueprint , render_template , request
from .models import *
views = Blueprint("views",__name__)

@views.route("/analyser",methods = ['GET','POST'])
@views.route("/",methods = ['GET','POST'])
def analyser():
    added = None
    if request.method == "POST":
        string = request.form["string"]
        print(string)
        added = Text(id=0,text = string , length = len(string),pos_analysis = {} , sentiment_analysis = "" , ner_analysis = {}).save() 
        print("record added")
    return render_template("analyzer.html",add = added)

@views.route("/dataset")
def dataset():
    data = Text.objects
    return render_template("data.html",data = data)