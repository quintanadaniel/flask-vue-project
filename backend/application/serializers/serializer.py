from application import ma


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "body", "create_at")
