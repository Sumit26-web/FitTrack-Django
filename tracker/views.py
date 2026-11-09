from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.utils import timezone
from .forms import RegisterForm, WorkoutForm, MealForm, GoalForm
from .models import Workout, Meal, FitnessGoal

def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "tracker/landing.html")

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Welcome to FitTrack! Your account is ready.")
        return redirect("dashboard")
    return render(request, "registration/register.html", {"form": form})

@login_required
def dashboard(request):
    today = timezone.localdate()
    week_start = today - timedelta(days=6)
    workouts = Workout.objects.filter(user=request.user)
    meals = Meal.objects.filter(user=request.user)
    today_workouts = workouts.filter(date=today)
    today_meals = meals.filter(date=today)
    week_workouts = workouts.filter(date__gte=week_start, date__lte=today)
    total_minutes = week_workouts.aggregate(v=Sum("duration"))["v"] or 0
    total_burned = week_workouts.aggregate(v=Sum("calories"))["v"] or 0
    eaten = today_meals.aggregate(v=Sum("calories"))["v"] or 0
    goals = FitnessGoal.objects.filter(user=request.user)
    chart_labels, chart_minutes, chart_calories = [], [], []
    for offset in range(6, -1, -1):
        day = today - timedelta(days=offset)
        day_qs = workouts.filter(date=day)
        chart_labels.append(day.strftime("%a"))
        chart_minutes.append(day_qs.aggregate(v=Sum("duration"))["v"] or 0)
        chart_calories.append(day_qs.aggregate(v=Sum("calories"))["v"] or 0)
    context = {
        "today": today, "workout_count": today_workouts.count(),
        "total_minutes": total_minutes, "total_burned": total_burned,
        "eaten": eaten, "recent_workouts": workouts[:5], "recent_meals": today_meals[:4],
        "goals": goals[:3], "chart_labels": chart_labels,
        "chart_minutes": chart_minutes, "chart_calories": chart_calories,
    }
    return render(request, "tracker/dashboard.html", context)

@login_required
def workout_list(request):
    items = Workout.objects.filter(user=request.user)
    return render(request, "tracker/workouts.html", {"items": items})

@login_required
def workout_add(request):
    form = WorkoutForm(request.POST or None, initial={"date": timezone.localdate()})
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False); item.user = request.user; item.save()
        messages.success(request, "Workout added successfully.")
        return redirect("workouts")
    return render(request, "tracker/form_page.html", {"form": form, "heading": "Log a workout", "subheading": "Every session counts.", "button": "Save workout"})

@login_required
def workout_delete(request, pk):
    item = get_object_or_404(Workout, pk=pk, user=request.user)
    if request.method == "POST":
        item.delete(); messages.success(request, "Workout deleted.")
    return redirect("workouts")

@login_required
def meal_list(request):
    items = Meal.objects.filter(user=request.user)
    return render(request, "tracker/meals.html", {"items": items})

@login_required
def meal_add(request):
    form = MealForm(request.POST or None, initial={"date": timezone.localdate()})
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False); item.user = request.user; item.save()
        messages.success(request, "Meal added successfully.")
        return redirect("meals")
    return render(request, "tracker/form_page.html", {"form": form, "heading": "Log a meal", "subheading": "Fuel your progress.", "button": "Save meal"})

@login_required
def meal_delete(request, pk):
    item = get_object_or_404(Meal, pk=pk, user=request.user)
    if request.method == "POST":
        item.delete(); messages.success(request, "Meal deleted.")
    return redirect("meals")

@login_required
def goal_list(request):
    items = FitnessGoal.objects.filter(user=request.user)
    return render(request, "tracker/goals.html", {"items": items})

@login_required
def goal_add(request):
    form = GoalForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        item = form.save(commit=False); item.user = request.user; item.save()
        messages.success(request, "Goal created. Keep going!")
        return redirect("goals")
    return render(request, "tracker/form_page.html", {"form": form, "heading": "Set a new goal", "subheading": "Small steps make big changes.", "button": "Create goal"})

@login_required
def goal_update(request, pk):
    item = get_object_or_404(FitnessGoal, pk=pk, user=request.user)
    form = GoalForm(request.POST or None, instance=item)
    if request.method == "POST" and form.is_valid():
        form.save(); messages.success(request, "Goal updated.")
        return redirect("goals")
    return render(request, "tracker/form_page.html", {"form": form, "heading": "Update goal", "subheading": "Adjust your target and progress.", "button": "Update goal"})

@login_required
def goal_delete(request, pk):
    item = get_object_or_404(FitnessGoal, pk=pk, user=request.user)
    if request.method == "POST":
        item.delete(); messages.success(request, "Goal deleted.")
    return redirect("goals")
