from django.urls import path
from book import views
urlpatterns = [
    path('getInfo/', views.query_book, name = "getInfo"),
    path('getInfoList/', views.query_book_list, name = "getInfoList")
]