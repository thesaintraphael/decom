from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from .forms import RegisterForm, LoginForm, ChangePassword, ChangeUsername
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# from django.core.mail import send_mail


# Create your views here.


def register(request):
    if request.user.is_authenticated:
        messages.info(request, 'You already have an account')
        return redirect('store:home')

    if request.method == "POST":
        form = RegisterForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')

            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()

            login(request, new_user)

            messages.success(request, 'You signed up successfully')
            # send_mail('Registration',
            #           'Congrats. You have successfully registered in our website. Enjoy by writing or reading '
            #           'articles that cover different topics!',
            #           'thesaintrapha@gmail.com',
            #           [email], fail_silently=False)

            return redirect("store:home")

        context = {
            'form': form,
        }
        return render(request, 'register.html', context)

    else:
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        messages.info(request, 'You have already logged in')
        return redirect('store:home')

    form = LoginForm(request.POST or None)

    context = {
        'form': form
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Invalid username or password')
            return render(request, 'login.html', context)

        messages.success(request, 'You signed in successfully')
        login(request, user)
        return redirect('store:home')

    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    messages.success(request, "You logged out successfully")
    return HttpResponseRedirect(reverse('store:home'))


def change_password(request, id):
    if not request.user.is_authenticated:
        messages.info(request, "You are not logged in")
        return redirect('user:login')

    elif request.user.id != id:
        messages.info(request, 'You cannot edit settings of another user')
        return redirect('store:home')

    if request.method == 'POST':
        form = ChangePassword(request.POST or None)

        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            old_password = form.cleaned_data.get('old_password')

            u = authenticate(username=request.user.username, password=old_password)

            if u:
                u.set_password(new_password)
                u.save()
                messages.success(request, 'Your password changed successfully. Please sign in again.')
                # send_mail('Password Configuration',
                #           'Your password has just successfully changed.',
                #           'thesaintrapha@gmail.com',
                #           [request.user.email], fail_silently=False)
                return redirect('user:login')
            else:
                messages.info(request, 'You entered your old password wrongly')
                context = {
                    'form': form,
                }

                return render(request, 'change_password.html', context)

        context = {
            'form': form,
        }

        return render(request, 'change_password.html', context)

    else:
        form = ChangePassword()
        context = {
            'form': form,
        }

        return render(request, 'change_password.html', context)


def change_username(request, id):
    if not request.user.is_authenticated:
        messages.info(request, 'You are not logged in')
        return redirect('user:login')

    elif request.user.id != id:
        messages.info(request, 'You cannot edit settings of another user')
        return redirect('store:home')

    if request.method == 'POST':
        form = ChangeUsername(request.POST or None)

        if form.is_valid():
            new_username = form.cleaned_data.get('new_username')

            u = User.objects.get(username=request.user.username)
            u.username = new_username
            u.save()
            messages.success(request, 'Your username is changed successfully')
            return redirect('store:home')

        context = {
            'form': form,
        }

        return render(request, 'change_username.html', context)

    else:
        form = ChangeUsername()
        context = {
            'form': form,
        }

        return render(request, 'change_username.html', context)
