from django.shortcuts import render
from myapp.models import student
# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')

def index2(request):
    if request.method =='POST':
       fname = request.POST.get('fname')
       email = request.POST.get('email')
       message = request.POST.get('message')
       s = student(firstname=fname,email=email,message=message)
       s.save()
    return render(request,'myapp/secondpage.html')