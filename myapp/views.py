from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'myapp/index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
       
    return render(request, 'myapp/login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        print("this is signup",username,email,password,confirm_password)
    return render(request,'myapp/signup.html')

def addtask(request):
    if request.method == "POST":
        title= request.POST.get("title")
        description = request.POST.get("description")
        date=request.POST.get("date")
       
    return render(request, 'myapp/addtask.html')

def updatetask(request):
    if request.method == "POST":
        title= request.POST.get("title")
        description = request.POST.get("description")
        date=request.POST.get("date")
       
    return render(request, 'myapp/updatetask.html')