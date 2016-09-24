
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_jwt.views import  obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/books/', include('modules.books.urls', namespace="books")),
    url(r'^api/houses/', include('modules.houses.urls', namespace="houses")),
    url(r'^api/creatures/', include('modules.creatures.urls', namespace="creatures")),

    # RUTA PARA AUTENTICACION
    url(r'^api-auth/', obtain_jwt_token),

]
