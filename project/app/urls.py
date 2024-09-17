from django.urls import path

from app import views

urlpatterns = [
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorDetail.as_view()),
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.BookDetail.as_view()),
    path('book_update/<int:pk>/', views.BookUpdate.as_view()),
    path('book_create/', views.BookCreate.as_view()),
    path('book_delete/<int:pk>/', views.BookDelete.as_view())
]