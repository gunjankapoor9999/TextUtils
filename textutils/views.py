# I have created this file - Gunjan Kapoor

from django.http import HttpResponse
from django.shortcuts import render


# code for video 6

# def index(request):
#     return HttpResponse("<h1>Hello</h1>")
#
#
# def about(request):
#     return HttpResponse("About")
#
#
# def existingFile(request):
#     # with open("one.txt") as f:
#     f = open("one.txt")
#     return HttpResponse(f.read())
#
#
# def navigator(request): return HttpResponse('''<h1>Navigate To</h1> <a href="https://www.google.com"> Google </a>
# <a href="https://www.youtube.com">Youtube</a>''')

# code for video 7

# def index(request):
#     return HttpResponse("Home")


def index(request):
    # code for video-8
    # dict = {'name': 'harry', 'place': 'earth'}
    # return render(request, "index.html", dict)

    # code for video-9
    return render(request, "index.html")


# code for video-9
# def removepunctuation(request):
#     # get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     # analyse the text
#     return HttpResponse("Remove punctuation")


def analyse(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunctuation', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    print(removepunc)
    print(djtext)
    # analyse the text
    # return HttpResponse("Remove punctuation")
    if removepunc == "on":
        # analysed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed = analysed + char
        params = {'purpose': 'Removed Punctuations', 'analysed_text': analysed}
        djtext = analysed
        # return render(request, 'analyse.html', params)


    if fullcaps == "on":
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()
        params = {'purpose': 'changeToUpperCase', 'analysed_text': analysed}
        djtext = analysed
        # return render(request, 'analyse.html', params)


    if newlineremover == "on":
        analysed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analysed = analysed + char
        params = {'purpose': 'newLineRemover', 'analysed_text': analysed}
        djtext = analysed
        # return render(request, 'analyse.html', params)


    if extraspaceremover == "on":
        analysed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analysed = analysed + char
        params = {'purpose': 'extraSpaceRemover', 'analysed_text': analysed}
        djtext = analysed
        # return render(request, 'analyse.html', params)



    if charcounter == "on":
        analysed = 0
        for char in djtext:
            analysed = analysed + 1
        params = {'purpose': 'charcount', 'analysed_text': analysed}
        djtext = analysed
        # return render(request, 'analyse.html', params)


    if charcounter != "on" and extraspaceremover == "on" and newlineremover == "on" and fullcaps == "on" and removepunc!= "on":
         return HttpResponse("choose something")

    return render(request, 'analyse.html', params)

# code for video-9
# def capitalizefirst(request):
#     return HttpResponse("Capitalize first")
#
#
# def newlineremove(request):
#     return HttpResponse("New line remover")
#
#
# def spaceremover(request):
#     return HttpResponse("Space remover <a href='/'>back</a>")
#
#
# def charcount(request):
#     return HttpResponse("Char count")
