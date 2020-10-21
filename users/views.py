from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# User Registration View
def registration(request):
    
    if request.method == 'POST':
        # Inherits forms.py 
         form = UserRegistrationForm(request.POST)
         if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account successfully created. You can Login from here')
            return redirect('login')
    else:         
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})



@login_required     # Restricts access if the user is not logged in
# User Profile View
def profile(request):
    return render(request, 'users/profile.html')
    