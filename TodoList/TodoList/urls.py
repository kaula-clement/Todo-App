
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('apis.urls')),
    path('',include('TodoApp.urls')) ,
    path('api-auth/', include('rest_framework.urls')) 

]
