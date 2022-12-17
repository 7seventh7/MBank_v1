from django.contrib import admin
from django.urls import path, include
from bank.views import UserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bank.urls')),
    path('api/customerlist', UserAPIView.as_view())
]
