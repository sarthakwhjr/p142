from flask import Flask,jsonify,request
import csv
from demographicfiltering import output
from contentfiltering import get_recommendations
allarticles=[]
with open("articles.csv", encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    allarticles=data[1:]

liked=[]
disliked=[]

app=Flask(__name__)
@app.route("/getarticles")
def getmovie():
    return jsonify({
        "data":allarticles[0],
        "status":"success",
    })
@app.route("/likedarticles",methods=["POST"])
def likedmovie():
    global allarticles
    movie=allarticles[0]
    allarticles=allarticles[1:]
    liked.append(movie)
    return jsonify({
        "status":"success"

    }),201 

@app.route("/dislikedarticles",methods=["POST"])
def dislikedmovie():
    global allarticles
    movie=allarticles[0]
    allmovies=allarticles[1:]
    disliked.append(movie)
    return jsonify({
        "status":"success"

    }),201

@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
            "url": article[0],
            "title": article[1],
            "text": article[2],
            "lang": article[3],
            "total_events": article[4]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked:
        output = get_recommendations(liked_article[4])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "url": recommended[0],
            "title": recommended[1],
            "text": recommended[2],
            "lang": recommended[3],
            "total_events": recommended[4]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200 
if (__name__=="__main__"):
    app.run()  