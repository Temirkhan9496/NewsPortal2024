from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('subscribe/', views.subscribe, name='subscribe'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]