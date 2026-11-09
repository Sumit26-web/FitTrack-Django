from django.urls import path
from . import views
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("workouts/", views.workout_list, name="workouts"),
    path("workouts/add/", views.workout_add, name="workout_add"),
    path("workouts/<int:pk>/delete/", views.workout_delete, name="workout_delete"),
    path("meals/", views.meal_list, name="meals"),
    path("meals/add/", views.meal_add, name="meal_add"),
    path("meals/<int:pk>/delete/", views.meal_delete, name="meal_delete"),
    path("goals/", views.goal_list, name="goals"),
    path("goals/add/", views.goal_add, name="goal_add"),
    path("goals/<int:pk>/edit/", views.goal_update, name="goal_update"),
    path("goals/<int:pk>/delete/", views.goal_delete, name="goal_delete"),
]
