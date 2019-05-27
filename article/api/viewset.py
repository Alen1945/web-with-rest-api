from rest_framework.generics import (ListAPIView,
									RetrieveAPIView,
									RetrieveUpdateAPIView,
									DestroyAPIView,
									CreateAPIView,
									)
from rest_framework.permissions import (
								AllowAny,
								IsAuthenticated,
								IsAuthenticatedOrReadOnly,
	)

from rest_framework.filters import SearchFilter
from .pagination import (ArticleLimitOffsetPagination,ArticlePageNumberPagination)
from article.models import ArticleModel
from .serializers import ArticleSerializer,CreateArticle
from .permissions import IsOwnerOrReadOnly

class ArticleAPIView(ListAPIView):
	serializer_class=ArticleSerializer
	filter_backends=[SearchFilter]
	search_fields=['title','body','user__username']
	pagination_class=ArticlePageNumberPagination
	def get_queryset(self,*args,**kwargs):
		query=ArticleModel.objects.all()
		return query.filter(user=self.request.user)



class CreateArticleAPIView(CreateAPIView):
	serializer_class=CreateArticle
	queryset=ArticleModel.objects.all()
	permission_classes=[IsAuthenticated]
	def perform_create(self,serializer):
		if serializer.is_valid():
			serializer.save(user=self.request.user)
class ArticleDetailAPIView(RetrieveAPIView):
	queryset=ArticleModel.objects.all()
	serializer_class=ArticleSerializer

class ArticleUpdateAPIView(RetrieveUpdateAPIView):
	queryset=ArticleModel.objects.all()
	serializer_class=CreateArticle
	permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class ArticleDeleteAPIView(DestroyAPIView):
	queryset=ArticleModel.objects.all()
	serializer_class=ArticleSerializer
	permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]