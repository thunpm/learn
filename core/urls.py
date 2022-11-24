from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classview/', include('classview.urls')),
    path('hrm/', include('hrm.urls')),
]
