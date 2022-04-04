from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
