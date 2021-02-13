# This file is created by Sujay.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    mylist = {'name':'Sujay', 'place':'India'}
    return render(request, 'index.html', mylist)

    # return HttpResponse("Home"
    #                     "<a href='/'> Back </a>")


def punc(request):
    djtext = request.POST.get('text', 'default')
    punc = request.POST.get('punc', 'off')
    caps = request.POST.get('caps', 'off')
    newline = request.POST.get('newline', 'off')

    if punc == "on":
        # analysed = djtext
        analysed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        mytext = {'purpose':'Removing Punctuations', 'analyse_text':analysed}
        return render(request, 'punc.html', mytext)

    elif caps=="on":
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        mytext = {'purpose': 'Capitalizing', 'analyse_text': analysed}
        return render(request, 'punc.html', mytext)

    elif newline=="on":
        analysed = ""
        for char in djtext:
            if char != "\n":
                analysed = analysed + char
            mytext = {'purpose':'Newline Remover', 'analyse_text': analysed}
            return render(request, 'punc.html', mytext)

    else:
        return HttpResponse("Error")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def newlinechar(request):
    return HttpResponse("New line character")


def capt(request):
    return HttpResponse("Capitalize")


def charcount(request):
    return HttpResponse("Character counting")



def details(request):
    return HttpResponse("Details will be uploaded here later on.")
