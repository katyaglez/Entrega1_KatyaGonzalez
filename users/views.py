from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import render

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form':form
        }
        return render(request, 'users/login.html', context=context)
    
    elif request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                context = {
                    'message': f'¡Bienvenido al portal de Aquatic Club {user}!'
                }
                return render(request,'pagina_inicio.html', context=context)
            
        form = AuthenticationForm()
        context ={
            'form':form,
            'errors': 'Usuario o contraseña incorrectos'
        }
        return render(request, 'users/login.html', context=context)
