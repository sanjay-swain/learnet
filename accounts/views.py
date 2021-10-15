from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import User
from .decorators import login_required_message


def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        valnext = request.POST.get('next')

        user = authenticate(username=email, password=password)

        if user is not None and valnext == '':
            messages.success(request, 'You successfully logged in!')
            login(request, user)
            return redirect('home')
        
        elif user is not None and valnext != '':
            messages.success(request, 'You successfully logged in!')
            login(request, user)
            return redirect(valnext)

        else:
            messages.error(request, 'Try again! username or password is incorrect')

    template_view = 'registration/login.html'
    return render(request, template_view, {})


@login_required_message(message="You can't logout if you haven't logged in the first place.")
@login_required(login_url="login")
def logout_page(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')


@login_required_message()
@login_required(login_url="login")
def user_profile(request, index):
    user_account = User.objects.get(id=index)
    return render(request, 'profile.html', {'user_account': user_account})
