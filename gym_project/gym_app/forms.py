from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Classe de formulari per al registre d'usuaris, que s'extén de UserCreationForm.
class UserRegistrationForm(UserCreationForm):
    # Camp d'email obligatori amb la seva etiqueta corresponent.
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        # S'indica que el model associat és User.
        model = User
        # Camps del formulari: inclou informació bàsica i els camps de contrasenya.
        fields = ('email', 'username', 'first_name', 'last_name', 'role', 'password1', 'password2')

# Formulari per a l'inici de sessió d'usuaris.
class UserLoginForm(forms.Form):
    # Camp per a l'email de l'usuari.
    email = forms.EmailField()
    # Camp per a la contrasenya, amb un input que oculta el text (password input).
    password = forms.CharField(widget=forms.PasswordInput)

# Formulari per editar el perfil de l'usuari.
class ProfileEditForm(forms.ModelForm):
    # Camp d'email obligatori amb la seva etiqueta corresponent.
    email = forms.EmailField(required=True, label='Email')
    # Camps per al nom i cognoms de l'usuari, amb longitud màxima.
    first_name = forms.CharField(label='Nom', max_length=30)
    last_name = forms.CharField(label='Cognoms', max_length=30)
    
    class Meta:
        # El model associat és User.
        model = User
        # Especifica els camps que es poden editar (username, email, first_name i last_name).
        fields = ('username', 'email', 'first_name', 'last_name')
