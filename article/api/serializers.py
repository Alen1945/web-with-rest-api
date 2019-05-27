from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField
from article.models import ArticleModel


class ArticleSerializer(ModelSerializer):
	url=HyperlinkedIdentityField(
		view_name='posts-api:detail',
		lookup_field='pk'
		)
	class Meta:
		model=ArticleModel
		fields=[
			'url',
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