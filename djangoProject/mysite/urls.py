from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', v.HomeView.as_view(), name='home'),
]
