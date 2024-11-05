from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from home.models import Patient, Donor

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user_obj = User.objects.filter(username=username)  # Corrected typo here
            if not user_obj.exists():
                messages.info(request, 'Account not found')
                return HttpResponse("Account not found")  # Replace "nothing" with relevant message
            
            user_obj = authenticate(username=username, password=password)
            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return render(request,'dashboard.html')
            
            messages.info(request, 'Invalid password')
            return redirect('/')
        
        return render(request, 'login.html')

    except Exception as e:
        print(e)
        return HttpResponse("An error occurred: {}".format(e))  # Return an HttpResponse in case of an exception



def dashboard(request):
    return render(request,'dashboard.html')

# users
def signusers(request):
    users=User.objects.all()
    return render(request, 'signusers.html', {'users':users})


# patient
def userpatient(request):
    patients=Patient.objects.all()
    # print(patients)
    return render(request, 'userpatient.html', {'patients':patients})

# donor
def userdonor(request):
    donors=Donor.objects.all()
    return render(request, 'userdonor.html', {'donors':donors})

def dashboard_view(request):
    user_count = User.objects.count()
    print(f'Total Users: {user_count}')  # Debugging line
    context = {
        'user_count': user_count,
    }
    return render(request, 'dashboard.html', context)