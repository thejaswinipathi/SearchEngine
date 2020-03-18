from django.urls import path
from book import views
urlpatterns = [
    path('getInfo/', views.query_book),
]