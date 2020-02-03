from datetime import date

import spiegel_scraper as spon
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/archive/<int:year>/<int:month>/<int:day>')
def archive(year: int, month: int, day: int):
    html = spon.archive.html_by_date(date(year, month, day))
    content = spon.archive.scrape_html(html)

    if request.args.get('include-html') is not None:
        return jsonify({
            'content': content,
            'html': html,
        })
    else:
        return jsonify(content)


@app.route('/articles')
def article():
    article_url = request.args.get('url')
    html = spon.article.html_by_url(article_url)
    content = spon.article.scrape_html(html)

    if request.args.get('include-html') is not None:
        return jsonify({
            'content': content,
            'html': html,
        })
    else:
        return jsonify(content)


@app.route('/articles/<article_id>/comments')
def article_comments(article_id: str):
    return jsonify(spon.comments.by_article_id(article_id))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
