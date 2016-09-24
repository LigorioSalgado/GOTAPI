from django.conf.urls import url
from .views import ListHouses, HouseDetail

urlpatterns = [
    url(r'^$', ListHouses.as_view()),
    url(r'^(?P<pk>[0-9]+)/$',HouseDetail.as_view())

]