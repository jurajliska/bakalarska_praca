# webova aplikacia pre system digitalnej prezencnej listiny. Addface - prijme encoding a ulozi ho do databazy.
# Knnupdate - z tvari v databze vytvori KNN klasfikator.
# Getnames - prijme encodingy, ktre pomocou KNN klasifikatora klasifikuje, priradi im mena. Tieto mena odosle naspat.

from flask import Flask, request, abort
import pymongo
import numpy as np
import pickle
from sklearn import neighbors
import math
import json

app = Flask(__name__)

myClient = pymongo.MongoClient("147.232.60.4:5901")
db = myClient["Liska"]
collection = db["faces"]


@app.route("/")
def index():
    return "Hello faces."


@app.route('/addface', methods=['POST'])
def new_face():
    if not request.json:
        abort(400)
    jejson = request.json
    collection.update_one({}, {"$set": jejson})

    return "Added"


@app.route('/knnupdate', methods=['GET'])
def knn_update():
    knn_algo = 'ball_tree'
    encodings = collection.find_one({}, {"_id": 0})

    names = list(encodings.keys())
    encods = np.array(list(encodings.values()))

    n_neighbros = int(round(math.sqrt(len(encods))))

    new_knn_clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbros, algorithm=knn_algo, weights='distance')
    new_knn_clf.fit(encods, names)

    with open('knn_model.clf', 'wb') as ff:
        pickle.dump(new_knn_clf, ff)

    return 'KNN Updated '


@app.route('/getnames', methods=['POST'])
def get_names():
    if not request.json:
        abort(400)

    data = request.json

    face_encodings = np.array(data.get("encodings"))

    with open('knn_model.clf', 'rb') as f:
        knn_clf = pickle.load(f)

    distance_threshold = 0.6

    closest_distances = knn_clf.kneighbors(face_encodings, n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(face_encodings))]
    """
    result = [(pred, loc) if rec else ("Unknown", loc) for pred, loc, rec in
              zip(knn_clf.predict(face_encodings), face_locations, are_matches)]
    """
    result = [pred if rec else "Unknown" for pred, rec in
              zip(knn_clf.predict(face_encodings), are_matches)]

    matches = 0
    for i in are_matches:
        if i:
            matches = matches + 1

    return json.dumps({"result": result, "matches": matches})


if __name__ == '__main__':
    app.run(debug=True)
