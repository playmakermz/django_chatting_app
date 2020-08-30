from django.shortcuts import render, redirect
from .models import *
# Create your views here.
# chat
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required


'''
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'password']
'''


@login_required(login_url='login')
def chat(request):
    note = pesan.objects.all()
    if request.method == 'POST':
        ab  = pesan(Pesan=request.POST['title'])
        ab.save()
        return redirect('/chat')

    main = {
    'note':note,

    }
    return render(request, '@chat/index.html', main)



def home(request):
    return render(request, '@HOME/index.html')


# ini untuk login
def sign_in(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
	main = {
        'please':'please sing in',
        'sing':'sing in'
    }
	return render(request, '@sign-in/index.html', main)



# ini untuk register
def sign_up(request):
    halo = '.'
    if request.user.is_authenticated:
        return redirect('/chat')
    else:
        form = User()
        if request.method == 'POST':
            #form = User(username=request.POST['username'], email='orang2163@gmail.com', password1=request.POST['password'], password2=request.POST['password'])
            username = request.POST['username']
            email = 'example@example.com'
            password = request.POST['password']

            form = User.objects.create_user(username, email, password)
            form.save()
            halo = 'terimakasih telah mendaftar'
            messages.success(request, 'Account was created for ')
            #return redirect('/')



    main = {
        'please':'please sing up',
        'sing':'sing up',
        'form':form,
        'halo':halo,
    }
    return render(request, '@sign-in/index.html', main)

# ini untuk logout 
def logout_user(request):
    logout(request)
    return redirect('login')
