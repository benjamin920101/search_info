from flask import Flask, render_template, request, jsonify
import requests
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    url = "https://article-extractor-and-summarizer.p.rapidapi.com/summarize"
    querystring = {
        "url": request.form['url'],
        "length": request.form['length'],
        "lang": "zh"
    }
    headers = {
        "X-RapidAPI-Key": "b496a8b32cmsh9623a9aef4812c5p1cbef0jsn9f3f3dfe6f6a",
        "X-RapidAPI-Host": "article-extractor-and-summarizer.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()
