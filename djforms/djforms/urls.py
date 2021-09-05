from django.contrib import admin

from django.urls import path

from books.views import (
    detail_book,
    delete_book,
    create_book,
    create_book_form,
    update_book,
    # book_home
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<pk>/', create_book, name='create-book'),
    path('htmx/create-book-form/', create_book_form, name='create-book-form'),
    path('htmx/book/<pk>/delete/', delete_book, name="delete-book"),
    path('htmx/book/<pk>/update/', update_book, name="update-book"),
    path('htmx/book/<pk>/', detail_book, name="detail-book"),
    # path('', book_home, name="book_home")
]