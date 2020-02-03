from datetime import date

import spiegel_scraper as spon
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/archive/<int:year>/<int:month>/<int:day>')
def archive(year: int, month: int, day: int):
    return jsonify(spon.archive.by_date(date(year, month, day)))


@app.route('/articles')
def article():
    article_url = request.args.get('url')
    return jsonify(spon.article.by_url(article_url))


@app.route('/articles/<article_id>/comments')
def article_comments(article_id: str):
    return jsonify(spon.comments.by_article_id(article_id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
