
#from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html")

def index2(request, val1):
    return render(request, "bookmodule/index2.html", {'val1': val1})

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)

# def index(request):
#    name = request.GET.get("name") or "world!"  # Add this line
 #   return HttpResponse("Hello, " + name)  # Replace the word "world!" with the variable name


#def index(request):
#    name = request.GET.get("name") or "world!"
 #   return render(request, "bookmodule/index.html")  # تغيير HttpResponse إلى دالة render


#def index2(request, val1=0):  # Add the view function (index2)
   # return HttpResponse("value1 = " + str(val1))
