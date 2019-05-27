from rest_framework.serializers import ModelSerializer
from article.models import ArticleModel


class ArticleSerializer(ModelSerializer):
	class Meta:
		model=ArticleModel
		fields=[
			'user',
			'id',
			'title',
			'body',
			'timestamp',
		]
class CreateArticle(ModelSerializer):
	class Meta:
		model=ArticleModel
		fields=['title','body']