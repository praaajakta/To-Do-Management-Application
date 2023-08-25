from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            # Provide feedback if login fails
            error_message = 'Invalid username or password. Please try again.'
    else:
        error_message = None  # No error message initially

    return render(request, 'user_login/registration.html', {'error_message': error_message})
