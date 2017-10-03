from django.conf.urls import url, include
from rest_framework import routers
from testapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
