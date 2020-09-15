from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'poll'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
]