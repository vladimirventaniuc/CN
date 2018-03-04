
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('tema_unu/', include('tema_unu.urls')),
    path('tema_doi/', include('tema_doi.urls')),
    path('tema_trei/', include('tema_trei.urls')),
    path('admin/', admin.site.urls),
]
