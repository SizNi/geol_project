from django.contrib import admin
from django.urls import path, include
from well_docs import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('crosses/', include('cross_section.urls')),
    path('admin/', admin.site.urls),
]
