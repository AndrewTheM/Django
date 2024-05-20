from django.urls import path
from app_blog import views

urlpatterns = [
    path(r'', views.HomePageView.as_view(), name='home'),
    path(r'articles', views.ArticleList.as_view(), name='articles-list'),
    path(r'articles/category/<slug>', views.ArticleCategoryList.as_view(), name='articles-category-list'),
    path(r'articles/<year>/<month>/<day>/<slug>', views.ArticleDetail.as_view(), name='news-detail'),
]
