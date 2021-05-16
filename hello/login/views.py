from django.shortcuts import render
from django.views import View
from . forms import CustomerRegistrationForm 
from django.contrib import messages
# Create your views here.

def profile(request):
    return render(request , 'login/profile.html')

class CustomerRegistrationView(View):
    def get(self , request):
        form = CustomerRegistrationForm()
        return render(request , 'login/customerregistration.html' , {'form':form})
    def post(self , request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request , 'Congratulations !! Successfully Registered')
            form.save()
        return render(request , 'login/customerregistration.html' , {'form':form})
