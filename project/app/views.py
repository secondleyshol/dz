from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView

from app.models import Author, Book
from app.serializer import AuthorSerializer, BookSerializer


# Create your views here.




class AuthorList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreate(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdate(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BookDelete(RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer