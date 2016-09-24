from django.conf.urls import url
from .views import ListCreatures

urlpatterns = [
    url(r'^$', ListCreatures.as_view()),


]