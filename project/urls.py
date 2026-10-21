from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),
    path(
        '',
        RedirectView.as_view(
            pattern_name='login',
            permanent=False
        ),
        name='home'
    ),
]