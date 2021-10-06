from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
            login(request, user)
            return redirect(valnext)

        else:
            messages.error(request, 'Try again! username or password is incorrect')

    template_view = 'registration/login.html'
    return render(request, template_view, {})


def logout_page(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')
