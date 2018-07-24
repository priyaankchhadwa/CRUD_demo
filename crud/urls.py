from django.urls import path

from . import views

app_name = 'crud'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:author_id>/', views.auth_details, name='auth_details'),
    path('new_auth', views.add_author, name='add_author'),
    path('edit_auth/<int:author_id>', views.edit_author, name='edit_author'),
    path('delete/<int:author_id>', views.delete_author, name='delete_author'),
    path('<int:author_id>/book/<int:book_id>', views.book_details, name='book_details')
]
