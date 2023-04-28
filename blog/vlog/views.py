from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView
from .models import Post
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from requests import *
from django.http import HttpResponse ,HttpResponseNotFound
class VlogListView(ListView):
    model = Post
    template_name = 'home.html'


class VlogDetailView(DeleteView):
    model = Post
    template_name = 'post.html'

def home(request):
    post = Post.objects.all()
    context = {
        'post': post
    }
    return render(request, 'blog/home.html', context)

def arab1(request):
   return render(request, 'arab.html')

def itbackend(request):
    return render(request, 'itbackend.html')
     
def itfrontend(request):
    return render(request, 'itfrontend.html')

def koresuz(request):
    return render(request, 'kores.html')

def tarix(request):
    return render(request, 'tarix.html')

def Rustli(request):
    return render(request, 'rustli.html')

def Onatli(request):
    return render(request, 'onatli.html')

def Matematika(request):
    return render(request, 'matematika.html')

def Kimyo(request):
    return render(request, 'kimyo.html')

def Biyologiya(request):
    return render(request, 'biyologiya.html')


def Ingliz(request):
    return render(request, 'ingliz.html')










# def Search(request):
# if request.method == 'POST':
#     search_text = request.POST['q']
#     if search_text:
#         post = Post.objects.filter(title__icontains=search_text) | Q(discrition__icontains=search_text)
#         context = {
#             'post': post
#         }
#         return render(request, 'blog/view_posts.html found')
#     else:
#         messages.error(request, 'Siz qdirgan malumot topilmadi!')
#         return redirect('view-posts')
# else:
#     return redirect('view-posts')
