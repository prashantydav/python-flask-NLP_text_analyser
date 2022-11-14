from flask import Blueprint , render_template , request

views = Blueprint("views",__name__)

@views.route("/analyser",methods = ['GET','POST'])
@views.route("/",methods = ['GET','POST'])
def analyser():
    string = request.form.get("string")
    print(string , "man")
    return render_template("analyzer.html")