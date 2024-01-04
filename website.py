from flask import Flask, render_template, request, jsonify
import requests
import os
import html

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/summarize', methods=['GET'])
def summarize_get():
    return "<meta http-equiv=\"refresh\" content=\"0;  url='/'\"/>"
@app.route('/summarize', methods=['POST'])
def summarize():
    url = "https://article-extractor-and-summarizer.p.rapidapi.com/summarize"
    if request.form['stop_python'] == "1":
        print("stop python")
        os._exit(0)
    querystring = {
        "url": request.form['url'],
        "length": "2",
        "lang": "zh",
    }
    headers = {
        "X-RapidAPI-Key": "b496a8b32cmsh9623a9aef4812c5p1cbef0jsn9f3f3dfe6f6a",
        "X-RapidAPI-Host": "article-extractor-and-summarizer.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    try:
        summary = response.json()['summary']
        html_summary = html.escape(summary)
        print(html_summary)
        html_summary = html_summary.replace('\n', '<br>')
        return html_summary
        #return jsonify(response.json())
    except KeyError:
        error = response.json()['error']
        html_error = html.escape(error)
        print(html_error)
        html_error = html_error.replace('\n', '<br>')
        return html_error

    
if __name__ == '__main__':
    app.run()
