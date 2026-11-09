from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Workout, Meal, FitnessGoal

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=40, required=False)
    class Meta:
        model = User
        fields = ("username", "first_name", "email", "password1", "password2")

class DateInput(forms.DateInput):
    input_type = "date"

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["activity", "duration", "calories", "distance", "date", "notes"]
        widgets = {"date": DateInput(), "notes": forms.TextInput(attrs={"placeholder": "How did it go?"})}

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["name", "meal_type", "calories", "protein", "date"]
        widgets = {"date": DateInput()}

class GoalForm(forms.ModelForm):
    class Meta:
        model = FitnessGoal
        fields = ["title", "goal_type", "target", "current", "deadline"]
        widgets = {"deadline": DateInput()}
