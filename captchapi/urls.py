from django.urls import path
from api import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/captcha', views.captcha, name="captcha"),
    path('api/captcha/<str:params>', views.captcha, name="captcha"),
]
