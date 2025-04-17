from django.shortcuts import render
from django.http.response import HttpResponse, Http404,HttpResponseNotFound, HttpResponseRedirect
#from django.http import HttpResponseRedirect

articles = {
        'Sports' : 'Sports Page',
        'Finance' : 'Finance Page',
        'Politics' : 'Politics'
    }


# Create your views here.
def welcome_view(request):
    return HttpResponse("<h1>Welcome to TIMES NOW!!<h1>")

def news_paper(request,topic):
    return HttpResponse(articles[topic])

def page_num_view(request, page_num):
    topics = list(articles.keys())
    topic = topics[page_num]
    return HttpResponseRedirect(topic)