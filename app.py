from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import random


def get_comments(shuffle):
    f = open('data.json', )
    data = json.load(f)
    comments = []
    for idx,comment in enumerate(data['comments']):
        if "@" in comment['text']:
            comments.append({
                "id": idx,
                "username": comment['owner']['username'],
                "profile_pic_url": comment['owner']['profile_pic_url'],
                "text": comment['text']
            })
    if shuffle:
        random.shuffle(comments)
    return comments


app = Flask(__name__)
CORS(app)


@app.route('/get-comments', methods=['POST'])
@cross_origin()
def hello_world():
    shuffle = request.get_json()['shuffle']
    comments = get_comments(shuffle)
    return {'comments': comments}
