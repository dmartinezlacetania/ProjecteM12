from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ExerciseForm, RoutineForm
from .models import Exercise, Routine
from bson import ObjectId
from djongo import models
from django.shortcuts import get_object_or_404

# Create your views here.

def is_trainer(user):
    return user.role == "trainer"


@user_passes_test(is_trainer)
@login_required
def exercise_list(request):
    exercises = Exercise.objects.all()
    return render(request, 'gym_trainer/exercise_list.html', {'exercises': exercises})

@user_passes_test(is_trainer)
@login_required
def exercise_create(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save
            return redirect('exercise_list')
    else:
        form = ExerciseForm()
    return render(request, 'gym_trainer/exercise_create_edit.html', {'form': form})

@user_passes_test(is_trainer)
@login_required
def exercise_edit(request, exercise_id=None):
    if exercise_id:  # Si se proporciona un ID, significa que estamos editando un ejercicio existente
        exercise = get_object_or_404(Exercise, id=exercise_id)
    else:  # Si no hay ID, estamos creando un ejercicio nuevo
        exercise = None

    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('gym_trainer:exercise_list')  # Redirigir a la lista de ejercicios tras guardar
    else:
        form = ExerciseForm(instance=exercise)  # Mostrar formulario vacío o prellenado con datos del ejercicio

    return render(request, 'gym_trainer/exercise_create_edit.html', {'form': form, 'exercise': exercise})

@user_passes_test(is_trainer)
@login_required
def routine_list(request):
    routines = Routine.objects.all()
    return render(request, 'gym_trainer/routine_list.html', {'routines': routines})

@user_passes_test(is_trainer)
@login_required
def routine_create(request):
    exercises = Exercise.objects.all()
    if request.method == 'POST':
        form = RoutineForm(request.POST)
        if form.is_valid():
            routine = form.save
            return redirect('gym_trainer:routine_list')
    else:
        form = RoutineForm()
    return render(request, 'gym_trainer/routine_create_edit.html', {'form':form} )