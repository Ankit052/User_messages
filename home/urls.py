from django.urls import path,include
from rest_framework.authtoken import views
from .views import MessageViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'',MessageViewSet, basename='message')

urlpatterns = [

     path('message/', include(router.urls)),
    path('token/login/', views.obtain_auth_token, name='create-token')
]