from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Donor
from .models import Patient
from .models import Product

import os

# Create your views here.

@login_required(login_url='handleLogin')
def main(request):
    products=Product.objects.all()
    params={'product':products}
    return render(request, 'main.html',params)

@login_required(login_url='handleLogin')
def contact(request):
    return render(request, 'contact.html')

@login_required(login_url='handleLogin')
def services(request):
    return render(request, 'services.html')

def index(request):
    return render(request, 'index.html')

@login_required(login_url='handleLogin')
def about(request):
    return render(request, 'about.html')

def Signup(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1!=password2:
            return HttpResponse("Password are not same !!!")
        else:
            # return redirect('login')
            my_user=User.objects.create_user(username=username,email=email,password=password1)
            my_user.save()
            # return HttpResponse("You have signup successfully ")

    return render(request, 'login.html')


def handleSignup(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 != pass2:
            return HttpResponse("Password not matching")


        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return render(request,'index.html')


    else:
        return HttpResponse("404 - Not Found")
    

@login_required(login_url='handleLogin')
def view_detail(request, id):
    product = Product.objects.filter(id=id)
    # print(product)
    return render(request, 'view_detail.html', {'product':product})
   

def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']
        # print(username,password1)
        user=authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('main')
        else:
            return HttpResponse("Username or password is incorrect")
    return redirect('main')


def handleLogout(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect('index')
    # return HttpResponse('handleLogout')



def donor(request, id=None):
    if id:
        donor = get_object_or_404(Donor, id=id)
    else:
        donor = None

    if request.method == 'POST':
        blood_group = request.POST.get('blood_group')
        donor_name = request.POST.get('dname')
        donor_contact = request.POST.get('dcontact')
        donor_address = request.POST.get('daddress')
        donor_disease = request.POST.get('ddisease')
        donor_city = request.POST.get('dcity')
        donor_zip = request.POST.get('dzip')
        donor_state = request.POST.get('dstate')

        if donor: 
            donor.blood_group = blood_group 
            donor.donor_name = donor_name
            donor.donor_contact = donor_contact
            donor.donor_address = donor_address
            donor.donor_disease = donor_disease
            donor.donor_city = donor_city
            donor.donor_zip_code = donor_zip
            donor.donor_state = donor_state
            donor.save()
        else:  
            Donor.objects.create(
                blood_group = blood_group,
                donor_name=donor_name,
                donor_contact=donor_contact,
                donor_address=donor_address,
                donor_disease=donor_disease,
                donor_city=donor_city,
                donor_zip_code=donor_zip,
                donor_state=donor_state
            )

        return render(request, 'thankyou.html')
    return render(request, 'name.html', {'donor': donor})


def patient(request):
    if request.method == 'POST':
        patient=Patient
        blood_group = request.POST.get('blood_group')
        quantity = request.POST.get('quantity')
        pname = request.POST.get('pname')
        pcontact = request.POST.get('pcontact')
        paddress = request.POST.get('paddress')
        pdesease = request.POST.get('pdesease')  
        hname = request.POST.get('hname') 
        hcontact = request.POST.get('hcontact')  
        haddress = request.POST.get('haddress')  
        city = request.POST.get('city')
        zip_code = request.POST.get('zip')
        state = request.POST.get('state')
        
        
        if blood_group and quantity and pname and pcontact and paddress:
            try:
                
                patient = Patient.objects.create(
                    blood_group=blood_group,
                    quantity=quantity,
                    patient_name=pname,
                    patient_contact=pcontact,
                    patient_address=paddress,
                    disease_name=pdesease,  
                    hospital_name=hname, 
                    hospital_contact=hcontact,
                    hospital_address=haddress,
                    hospital_city=city,
                    zip_code=zip_code,
                    state=state
                )
                patient.save()
                return render(request, 'thankyou.html')

            except Exception as e:
                
                return HttpResponse(f"An error occurred: {str(e)}")
        else:
            return HttpResponse("Missing required fields")

    return render(request, 'main.html')


def thankyou(request):
    return render(request, 'thankyou.html')

def status(request):
    return render(request, 'status.html')

def handle_upd(file,filename):
    if not os.path.exists('../BLOOD_BANK/static/upload/'):
        os.mkdir('../BLOOD_BANK/static/upload/')
    with open('../BLOOD_BANK/static/upload/'+filename,'wb+') as dest:
        for c in file.chunks():
            dest.write(c)

# def upd(request):
#     if request.method=="POST":
#         handle_upd(request.FILES['a2'],str(request.FILES['a2']))
#         url="upload/"+str(request.FILES['a2'])
#         u=picfile()  
#         u.pname=request.POST['a1']
#         u.purl=url.save()
#         return redirect("../upload")
    
