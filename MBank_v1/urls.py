from django.contrib import admin
from django.urls import path, include, re_path
from bank.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bank.urls')),

    path('api/userlist', AllUsersAPIView.as_view()),
    path('api/userlist/<int:pk>', SingleUserAPIView.as_view()),

    path('api/account/all', ListAccountAPI.as_view()),
    path('api/acoount/user/<int:pk>', AccountAPIUser.as_view()),
    path('api/account/admin/<int:pk>', AccauntAPIAdmin.as_view()),

    path('transfer_alt/', TransactionAPI.as_view()),


    path('api/v1/sdrf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
