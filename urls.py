from django.urls import path
   from .views import category_detail, subscribe_to_category

   urlpatterns = [
       path('category/<int:pk>/', category_detail, name='category_detail'),
       path('category/<int:pk>/subscribe/', subscribe_to_category, name='subscribe_to_category'),
   ]
