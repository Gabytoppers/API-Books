from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.

@csrf_exempt
def books( request ):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})
    
    elif request.method == 'POST':
        titulo= request.POST.get('titulo')
        autor = request.POST.get('autor')
        prrecio = request.POST.get('precio')

        #crear una instancia de Book con los datos recibidos
        book = Book(titulo=titulo, autor=autor, precio=precio)

        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)
        
        return JsonResponse(model_to_dict(book), status=201)

