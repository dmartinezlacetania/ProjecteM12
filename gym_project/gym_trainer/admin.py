from django.contrib import admin
from .models import Exercise, Routine
from .forms import ExerciseForm, RoutineForm

class ExerciseAdmin(admin.ModelAdmin):
    form = ExerciseForm  # Usa el formulari personalitzat
    list_display = ('name',)  # Mostra el nom a la llista d'ítems
    search_fields = ('name',)  # Permet buscar pel nom


class RoutineAdmin(admin.ModelAdmin):
    form = RoutineForm  # Usa el formulari personalitzat
    list_display = ('name',)  # Mostra el nom de la rutina
    search_fields = ('name',)  # Permet buscar pel nom
    filter_horizontal = ('exercises',)  # Facilita la selecció de múltiples exercicis

# Registra els models amb les configuracions personalitzades
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Routine, RoutineAdmin)
