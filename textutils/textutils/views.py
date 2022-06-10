# I have created this file harry

from django.http import HttpResponse
from django.shortcuts import render
#code for video 6
#def index(request):
  #  return HttpResponse('''<h1>Hello sarthak</h1> <a href="https://www.youtube.com/watch?v=Jksh4plnL5k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=15&ab_channel=CodeWithHarry">youtube</a>''')

#def about(request):
  #  return HttpResponse()

#def footer(request):
  #  return HttpResponse("How i  can help u")

#code for video 7

def ex1(request):
    s="<h1> welcome to Navigation bar</h1><br>" \
      "<a href="">facebook</a><br>" \
      "<a href="">youtube</a><br>" \
      "<a href="">google</a><br>" \
      "<a href="">yahoo</a>"
    return  HttpResponse(s)


def example2(request):
     return HttpResponse('''<h1 style="text-align:center;font-size:50px;color:red;position:relative;top:200px">does not find any punctuations</h1>''')


def index(request):

    return render(request,'index.html')
   # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    print(removepunc)
    print(djtext)
    if removepunc=="on":

       # analyzed=djtext
       punctuations='''!()-[]{},:'"\,<>./?@#$%^&*_~'''
       analyzed= " "
       for char in djtext:
           if char  not in punctuations:
               analyzed=analyzed+char
       params={'purpose':'-','analyzing_text':analyzed}

       # Analyze the text

       return render(request,'analyze.html',params)

    else:
       return HttpResponse('''<h1 style="text-align:center;font-size:50px;color:red;position:relative;top:200px">does not find any punctuations</h1>''')




    #Analyze the text
#     return  HttpResponse("remove punc")
# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")
# def newlineremove(request):
#     return HttpResponse("new line remove")
# def spaceremove(request):
#     return HttpResponse("Space remover <a href='/'>back</a>")
# def counter(request):
#     return HttpResponse("counter called")