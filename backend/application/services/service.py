from flask import jsonify, request
from application import app
from application.models.model import Articles

from application import db
from application.services import articles_schema, article_schema


@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "test first endpoint"})


@app.route("/get", methods=["GET"])
def get_articles():
    all_articles = Articles.query.all()
    result = articles_schema.dump(all_articles)
    return jsonify(result)


@app.route("/get/<id>/", methods=["GET"])
def get_article(id):
    article = Articles.query.get(id)
    result = article_schema.dump(article)
    return jsonify(result)


@app.route("/add", methods=["POST"])
def add_article():
    title = request.json["title"]
    body = request.json["body"]

    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()

    return article_schema.jsonify(articles)


@app.route("/update/<id>/", methods=["PUT"])
def update_article(id):
    article = Articles.query.get(id)
    title = request.json["title"]
    body = request.json["body"]

    article.title = title
    article.body = body

    db.session.commit()
    return article_schema.jsonify(article)


@app.route("/delete/<id>/", methods=["DELETE"])
def article_delete(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return article_schema.jsonify(article)
