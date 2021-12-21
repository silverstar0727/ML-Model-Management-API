from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=200, default="")
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "project"

class Models(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    model_name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, default="")
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "models"

class Experiments(models.Model):
    model_id = models.ForeignKey(Models, on_delete=models.CASCADE, null=False)
    parameters = models.CharField(null=False, max_length=1024)
    training_data_path = models.CharField(max_length=255, null=False)
    validation_data_path = models.CharField(max_length=255, null=False)
    test_data_path = models.CharField(max_length=255, null=False)
    evaluation = models.FloatField(null=True)
    artifact_file_path = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "experiments"