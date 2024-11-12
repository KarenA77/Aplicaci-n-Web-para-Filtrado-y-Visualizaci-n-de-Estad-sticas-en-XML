from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('inicio/',inicio),
    path('', include('myapp.urls'))
]