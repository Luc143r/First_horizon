from django.shortcuts import render
from .models import Articles

# Create your views here.


def post_list(request):
    articles = Articles.objects.all()
    return render(request, 'about_app/index.html', {'articles': articles})

def about_page(request):
    articles = Articles.objects.all()
    return render(request, 'about_app/about_page.html', {'articles': articles})