from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
import os

class UploadBookView(views.APIView):
    def post(self, request, *args, **kwargs):
        book_data = request.data
        book_serializer = BookSerializer(data=book_data)

        if book_serializer.is_valid():
            book_serializer.save()

            # Rename files after saving them
            book = Book.objects.get(id=book_serializer.instance.id)
            new_filename = book.title.replace(' ', '_')

            book.pdf.name = os.path.join('books', new_filename + '.pdf')
            book.cover_image.name = os.path.join('books', new_filename + '.jpg')

            book.save()

            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListBooksView(views.APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
