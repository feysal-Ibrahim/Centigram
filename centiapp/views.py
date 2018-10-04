from django.shortcuts import render
from django.http import HttpResponse , Http404  # import the HttpResponse class from the django.http module.
from peewee import DoesNotExist
from django.contrib.auth.decorators import login_required
from .models import Image


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images=Image.objects.all( )
    print( images )
    return render( request , 'index.html' , {"images": images} )


def about(request):
    return render( request , 'developer.html' )


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term=request.GET.get( "image" )
        searched_articles=Image.search_by_likes( search_term )
        message=f"{search_term}"

        return render( request , 'search.html' , {"message": message , "articles": searched_articles} )

    else:
        message="You haven't searched for any term"
        return render( request , 'search.html' , {"message": message} )
