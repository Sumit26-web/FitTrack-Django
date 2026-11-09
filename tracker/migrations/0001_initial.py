from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name="Workout", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("activity", models.CharField(choices=[("Running","Running"),("Walking","Walking"),("Cycling","Cycling"),("Strength","Strength training"),("Yoga","Yoga"),("Swimming","Swimming"),("HIIT","HIIT"),("Other","Other")], max_length=30)),
            ("duration", models.PositiveIntegerField(help_text="Duration in minutes")),
            ("calories", models.PositiveIntegerField(default=0)),
            ("distance", models.DecimalField(decimal_places=2, default=0, help_text="Distance in km", max_digits=7)),
            ("notes", models.CharField(blank=True, max_length=240)),
            ("date", models.DateField()),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="workouts", to=settings.AUTH_USER_MODEL)),
        ], options={"ordering":["-date","-created_at"]}),
        migrations.CreateModel(name="Meal", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=100)),
            ("meal_type", models.CharField(choices=[("Breakfast","Breakfast"),("Lunch","Lunch"),("Dinner","Dinner"),("Snack","Snack")], max_length=20)),
            ("calories", models.PositiveIntegerField()),
            ("protein", models.PositiveIntegerField(default=0, help_text="Protein in grams")),
            ("date", models.DateField()),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="meals", to=settings.AUTH_USER_MODEL)),
        ], options={"ordering":["-date","-created_at"]}),
        migrations.CreateModel(name="FitnessGoal", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=100)),
            ("goal_type", models.CharField(choices=[("Weight","Weight"),("Steps","Steps"),("Workout minutes","Workout minutes"),("Calories","Calories burned")], max_length=30)),
            ("target", models.PositiveIntegerField()),
            ("current", models.PositiveIntegerField(default=0)),
            ("deadline", models.DateField(blank=True, null=True)),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="fitness_goals", to=settings.AUTH_USER_MODEL)),
        ]),
    ]
