
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from books.views import UploadBookView, ListBooksView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('djoser.urls')),
    path('api/',include('users.urls')),
    path('api/upload/', UploadBookView.as_view()),
    path('api/books/', ListBooksView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
