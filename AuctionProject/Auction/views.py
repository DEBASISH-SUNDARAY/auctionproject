from django.shortcuts import redirect, render , HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login
from .forms import AddProduct
from .models import Product , Customer
# Create your views here.





def home(request):
    prod=Product.objects.all()
    return render(request,'home.html', {'prd':prod})
 
def home1(request):
    
    return render(request,'home1.html')

def userlogin(request):
    if request.method=='POST':
        lusername=request.POST.get('luname')
        lpassword=request.POST.get('lpsw')
        
        username=Customer.objects.all()
        prod1=Product.objects.all()
        for i in username:
           # print(type(i))
            if i.UserName==lusername and i.Password==lpassword:
                return render (request ,'home1.html',{'prd1':prod1})
            
        
    return render(request,'login.html')
    
def signup(request):

    if request.method=="POST":
        username=request.POST.get("uname")
        firstname=request.POST.get("fname")
        lastname=request.POST.get("lname")
        mob=request.POST.get("mob")
        email=request.POST.get("email")
        psw=request.POST.get("psw")
        cpsw=request.POST.get("cpsw")
        if psw != cpsw:
            return render (request,'signup.html')
        else:
            newuser=Customer(UserName=username,FirstName=firstname,LastName=lastname,MobileNo=mob,EmailId=email,Password=psw)
            newuser.save()
            messages.success(request , 'You have been registered Successfully')

       
        return redirect('userlogin')

    return render(request,'signup.html')


def myproduct(request):
    return render(request ,'myproduct.html')

def addproduct(request):

    if request.method == 'POST':
        prname= request.POST.get("prname")
        primage=request.POST.get("primage")
        datetime=request.POST.get("datetime")
        prdesc=request.POST.get("prdesc")
        newproduct=Product(ProductName=prname,ProductImage=primage, DateTime = datetime,Description=prdesc)
        newproduct.save()
    
    return render(request , 'addproduct.html')

def more(request):
    return render(request , 'more.html')