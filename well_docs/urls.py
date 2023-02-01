from django.contrib import admin
from django.urls import path
from well_docs import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
