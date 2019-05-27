from rest_framework.generics import (ListAPIView,
									RetrieveAPIView,
									UpdateAPIView,
									DestroyAPIView,
									CreateAPIView,
									)
from article.models import ArticleModel
from .serializers import ArticleSerializer,CreateArticle


class ArticleAPIView(ListAPIView):
	serializer_class=ArticleSerializer
	queryset=ArticleModel.objects.all()

class CreateArticleAPIView(CreateAPIView):
	serializer_class=CreateArticle
	queryset=ArticleModel.objects.all()
	def perform_create(self,serializer):
		if serializer.is_valid():
			serializer.save(user=self.request.user)
class ArticleDetailAPIView(RetrieveAPIView):
	queryset=ArticleModel.objects.all()
	serializer_class=ArticleSerializer

class ArticleUpdateAPIView(UpdateAPIView):
	queryset=ArticleModel.objects.all()
	serializer_class=CreateArticle

class ArticleDeleteAPIView(DestroyAPIView):
	queryset=ArticleModel.objects.all()
	serializer_class=ArticleSerializer
