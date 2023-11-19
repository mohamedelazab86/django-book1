from django.shortcuts import render
from .models import Book

# Create your views here.
 # ================================ create class based view =================

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


class list_book(ListView):                                 # CONTEXT IN TEMPLTES   IS name of model_list      (book_list or object_list)
    model=Book                                             # templates     name_actions                        (books_detail)

class detail_book(DetailView):                              # context in templates   is name_model               book      object
    model=Book                                              # templates           name_model  _action            book_detail

class create_book(CreateView):
    model=Book
    fields='__all__'
    success_url='/books/'
    template_name='books/create.html'

class update_book(UpdateView):
    model=Book
    fields='__all__'
    success_url='/books/'
    template_name='books/edit.html'
class delete_book(DeleteView):
    model=Book
    success_url='/books/'
    template_name='books/delete.html'




