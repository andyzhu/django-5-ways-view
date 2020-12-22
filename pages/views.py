from pages.models import Post
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, DetailView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

def home_page_view_function_based(request):
    return render(request, 'pages/home_function.html')

def home_page_view_no_template(request):
    return HttpResponse('<h1>Hello World from No Template View</h1>')

class HomeDetailView(DetailView): # 5. Model Based View
    model = Post
    template_name = 'pages/home_model.html'