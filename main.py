import csv
from flask import Flask,jsonify
from demographic_filtering import output
from content_filtering import get_recommendations

with open('final.csv',encoding='UTF-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articals = data[1:]

liked_articals = []
unliked_articals = []

app = Flask(__name__)

@app.route("/like")
def like_artical():
    artical = all_articals[0]
    liked_articals.append(artical)
    return jsonify({
        "status":'success'
    }),201

@app.route("/unlike")
def like_artical():
    artical = all_articals[0]
    unliked_articals.append(artical)
    return jsonify({
        "status":'success'
    }),201

@app.route("/popular")
def popular_articals():
    artical_data = []
    for artical in output:
        _d = {
            "title": artical[3],
            "rating": artical[21]
        }
        artical_data.append(_d)
    return jsonify({
        "data": artical_data,
        "status": "success"
    }), 200

@app.route("/recommended")
def recommended_articals():
    all_recommended = []
    for liked in like_artical:
        output = get_recommendations(liked[2])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    artical_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[2],
            "rating": recommended[21],
        }
        artical_data.append(_d)
    return jsonify({
        "data": artical_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
    app.run()