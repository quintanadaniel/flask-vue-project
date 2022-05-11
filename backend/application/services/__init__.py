from application.serializers.serializer import ArticleSchema


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
