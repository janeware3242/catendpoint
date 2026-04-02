from django.urls import include, path
from rest_framework import routers

from catpi.cats import views

router = routers.DefaultRouter()
router.register(r"cats", views.CatViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path("", include(router.urls)),
]
