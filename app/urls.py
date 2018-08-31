from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    # メニュー (Top)
    path('', views.index, name='index'),  # メニュー
]
