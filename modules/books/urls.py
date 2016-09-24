from django.conf.urls import url
from .views import ListBooks

urlpatterns = [
    url(r'^$', ListBooks.as_view()),


]