from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.all_books, name='books'),
    path('<book_id>/', views.book_detail, name='book_detail'),
]
