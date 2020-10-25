from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

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
    if request.method == 'POST':
        userUpdateForm = UserUpdateForm(request.POST, instance= request.user)
        profileUpdateForm = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if userUpdateForm.is_valid() and profileUpdateForm.is_valid():
            userUpdateForm.save()
            profileUpdateForm.save()
            messages.success(request, f"account has been updated")
            return redirect('profile')
    else:
        userUpdateForm = UserUpdateForm(instance= request.user)
        profileUpdateForm = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'uUpdateForm': userUpdateForm,
        'pUpdateForm': profileUpdateForm
    }
    return render(request, 'users/profile.html', context)
