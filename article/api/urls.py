from django.urls import path

from .viewset import (ArticleAPIView,
					ArticleDetailAPIView,
					ArticleDeleteAPIView,
					ArticleUpdateAPIView,
					CreateArticleAPIView,
					)
app_name='article'
urlpatterns=[
	path('',ArticleAPIView.as_view(),name='article_list'),
	path('create/',CreateArticleAPIView.as_view()),
	path('<pk>/',ArticleDetailAPIView.as_view(),name='detail'),
	path('<pk>/update/',ArticleUpdateAPIView.as_view()),
	path('<pk>/delete/',ArticleDeleteAPIView.as_view()),
]