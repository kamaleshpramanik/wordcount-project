from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')


def countpage(request):
    wordlist = request.GET['FullText']
    wordcount = wordlist.split()
    return render(request, 'count.html', {'wordlist':wordlist , 'wcount':len(wordcount)})

def aboutpage(request):
    return render(request, 'about.html')