from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name='Clothes/index.html'
    context_object_name = 'latest_art_list'
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')[:6]
