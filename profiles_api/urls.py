from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,basename='hello-viewset')

router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet,basename='login')
router.register('feed',views.UserProfileFeedViewSet)




urlpatterns = [

	url('hello-view/',views.HelloApiView.as_view()),
	url('',include(router.urls)),
]