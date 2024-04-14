from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello_viewset')
router.register('profile', views.UserProfileViewSet, base_name='profile_viewset')


urlpatterns = [
    path('hello-view/', views.HelloAPiView.as_view(), name='hello_view'),
    path('login/', views.UserLoginView.as_view(), name='login_view'),
    path('', include(router.urls))
]