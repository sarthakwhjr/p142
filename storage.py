import csv
allarticles = []
with open("articles.csv",encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    allarticles = data[1:]
likedarticles = []
notlikedarticles = []