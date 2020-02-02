from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User

# registration form
# user django user registration form
# no need to reinvent the wheel


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # check if valid
            form.save()  # save user info
            username = form.cleaned_data.get('username')  # get username
            messages.success(
                request, f'Your account has been created. You are now able to login.')
            return redirect('/users/login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Register'})


def login(request):
    return render(request, 'users/login.html', {'title': 'Login'})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            #messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

@login_required
def view_profile(request, pk = None):
    
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
        
    u_form = UserUpdateForm(instance=user)
    p_form = ProfileUpdateForm(instance=user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user
    }
    if pk: return render(request, 'users/profile_others.html', context)
    else : return render(request, 'users/profile.html', context)

# possible messages
# message.debug
# message.info
# message.success
# message.warning
# message.error
