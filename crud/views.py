from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Author, Book

from django.forms import ModelForm

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['salutation', 'author_name', 'gender', 'phone']


def index(request):
    author_list = Author.objects.all()
    context = {'author_list': author_list}
    return render(request, 'crud/index.html', context)

def auth_details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'crud/auth_details.html', {'author': author})

def add_author(request):
    # author = get_object_or_404(Author, pk=author_id)
    
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crud:index')
    return render(request, 'crud/add_author.html', {'form':form})

def edit_author(request, author_id):
    author = get_object_or_404(Author,  pk=author_id)
    form = AuthorForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        return redirect('crud:index')
    return render(request, 'crud/add_author.html', {'form': form})

def delete_author(request, author_id):
    author = get_object_or_404(Author,  pk=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('crud:index')
    return render(request, 'crud/auth_delete.html', {'object': author})

def book_details(request, author_id, book_id):
    print(book_id)
    try:
        book = Author.objects.get(pk=author_id).book_set.get(pk=book_id)
    except Exception as ex:
        print(ex)
    else:
        context = {'book': book}
        return render(request, 'crud/book_details.html', context)
    
    