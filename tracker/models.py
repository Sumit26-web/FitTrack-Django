from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    ACTIVITY_CHOICES = [
        ("Running", "Running"), ("Walking", "Walking"), ("Cycling", "Cycling"),
        ("Strength", "Strength training"), ("Yoga", "Yoga"), ("Swimming", "Swimming"),
        ("HIIT", "HIIT"), ("Other", "Other"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts")
    activity = models.CharField(max_length=30, choices=ACTIVITY_CHOICES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories = models.PositiveIntegerField(default=0)
    distance = models.DecimalField(max_digits=7, decimal_places=2, default=0, help_text="Distance in km")
    notes = models.CharField(max_length=240, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.activity} ({self.date})"

class Meal(models.Model):
    MEAL_CHOICES = [("Breakfast", "Breakfast"), ("Lunch", "Lunch"), ("Dinner", "Dinner"), ("Snack", "Snack")]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="meals")
    name = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField(default=0, help_text="Protein in grams")
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.name} - {self.calories} kcal"

class FitnessGoal(models.Model):
    GOAL_CHOICES = [("Weight", "Weight"), ("Steps", "Steps"), ("Workout minutes", "Workout minutes"), ("Calories", "Calories burned")]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="fitness_goals")
    title = models.CharField(max_length=100)
    goal_type = models.CharField(max_length=30, choices=GOAL_CHOICES)
    target = models.PositiveIntegerField()
    current = models.PositiveIntegerField(default=0)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def percentage(self):
        if not self.target:
            return 0
        return min(100, round(self.current / self.target * 100))
