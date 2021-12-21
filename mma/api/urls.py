from django.urls import path
from .views import CreateProject, CreateModel, CreateExperiment

urlpatterns = [
    path("create_project", CreateProject.as_view(), name="create_project"),
    path("create_model", CreateModel.as_view(), name="create_model"),
    path("create_experiment", CreateExperiment.as_view(), name="create_experiment")
]