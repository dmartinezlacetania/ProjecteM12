from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, ProfileEditForm

# Vista per registrar un nou usuari
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # S'instància el formulari amb les dades del POST
        if form.is_valid():  # Si el formulari és vàlid
            user = form.save()  # S'emmagatzema el nou usuari
            login(request, user)  # S'inicia la sessió automàticament després de registrar-se
            messages.success(request, 'Reistre completat amb exit!')  # Missatge d'èxit
            return redirect('home')  # Redirigeix a la pàgina d'inici
        else:
            messages.error(request, 'Error en el registre. Si us plau, corregeix els errors.')  # Missatge d'error
    else:
        form = UserRegistrationForm()  # Si és un GET, es mostra el formulari buit
    return render(request, 'gym_app/register.html', {'form': form})  # Renderitza la pàgina amb el formulari

# Vista per a l'inici de sessió
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)  # Instància el formulari amb les dades del POST
        if form.is_valid():  # Si el formulari és vàlid
            email = form.cleaned_data.get('email')  # Obté l'email netejat
            password = form.cleaned_data.get('password')  # Obté la contrasenya netejada
            user = authenticate(request, email=email, password=password)  # Intenta autenticar l'usuari
            if user is not None:  # Si l'usuari és trobat
                login(request, user)  # Inicia la sessió
                messages.success(request, 'Has iniciat sessió correctament!')  # Missatge d'èxit
                return redirect('home')  # Redirigeix a la pàgina d'inici
            else:
                messages.error(request, 'Email o contrasenya incorrectes.')  # Missatge d'error si l'autenticació falla
    else:
        form = UserLoginForm()  # Si és un GET, es mostra el formulari buit
    return render(request, 'gym_app/login.html', {'form': form})  # Renderitza la pàgina d'inici de sessió

# Vista per a la pàgina d'inici, només accessible si l'usuari està autenticat
@login_required
def home(request):
    return render(request, 'gym_app/home.html')  # Renderitza la pàgina d'inici

# Vista per tancar la sessió
def logout_view(request):
    logout(request)  # Tanca la sessió de l'usuari
    return redirect('home')  # Redirigeix a la pàgina d'inici després de tancar la sessió

# Vista per editar el perfil de l'usuari, només accessible si l'usuari està autenticat
@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)  # Instància el formulari amb les dades del POST i l'usuari actual
        if form.is_valid():  # Si el formulari és vàlid
            form.save()  # Desa els canvis al perfil de l'usuari
            messages.success(request, 'Perfil actualitzat correctament!')  # Missatge d'èxit
            return redirect('home')  # Redirigeix a la pàgina d'inici
        else:
            messages.error(request, 'Error en actualitzar el perfil. Si us plau, corregeix els errors.')  # Missatge d'error
    else:
        form = ProfileEditForm(instance=request.user)  # Si és un GET, es mostra el formulari amb les dades actuals de l'usuari
    return render(request, 'gym_app/profile_edit.html', {'form': form})  # Renderitza la pàgina d'edició de perfil
