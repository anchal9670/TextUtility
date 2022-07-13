from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
#test 1
#def index(request):
#    return HttpResponse('''hello <a href="https://www.youtube.com/watch?v=GADlWyHaMmI" >Pasoori</a>''')
#def about(request):
#    return HttpResponse("About Anchal")

def index(request):
    return render(request,'index.html')
def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    params={'purpose':'No changes','analyzed_text':djtext}
    if removepunc=="on":
        analyzed=""
        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_-'''
        for char in djtext:
            if char not in punctuation:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        #analyze the text 
        #return render(request, 'analyze.html',params)
        djtext=analyzed
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Change to uppercase','analyzed_text':analyzed}
        #analyze the text 
        #return render(request, 'analyze.html',params)
        djtext=analyzed
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed+char
            
        params={'purpose':'remove new line','analyzed_text':analyzed}
        #return render(request,'analyze.html',params)
        djtext=analyzed
    if extraspaceremover=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        params={'purpose':'space remover','analyzed_text':analyzed}
        #return render(request,'analyze.html',params)
        djtext=analyzed
    if charcount=='on':
        n=djtext, '=> ' ,len(djtext)  
        params={'purpose':'space remover','analyzed_text':n}
        #return render(request,'analyze.html',params)
    return render(request,'analyze.html',params)

#def capfirst(request):
    #return HttpResponse("capitalize first <a href='/'>back</a>")
#def newlineremove(request):
    #return HttpResponse("newline remove <a href='/'>back</a>")
#def spaceremove(request):
    #return HttpResponse("space remove <a href='/'>back</a>")
#def charcount(request):
    #return HttpResponse("char count <a href='/'>back</a>")
