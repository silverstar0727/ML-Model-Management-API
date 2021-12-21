import json
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import (
    Project,
    Models,
    Experiments
)

class CreateProject(APIView):
    def post(self, request):
        project_name = request.data.get("project_name", "")
        description = request.data.get("description", "")

        if Project.objects.filter(project_name=project_name).exists():
            return Response(status=403, data={"msg": "이미 존재하는 프로젝트입니다."})

        Project.objects.create(project_name=project_name,
                               description=description)

        data = {
            "project_name": project_name,
            "description": description
        }

        return Response(status=201, data=data)

class CreateModel(APIView):
    def post(self, request):
        project_name = request.data.get("project_name", "")
        model_name = request.data.get("model_name", "")
        description = request.data.get("description", "")


        if not Project.objects.filter(project_name=project_name).exists():
            return Response(status=403, data={"msg": "존재하지 않는 프로젝트명 입니다."})

        if Models.objects.filter(model_name=model_name).exists():
            return Response(status=403, data={"msg": "이미 존재하는 모델 이름입니다."})

        projects = Project.objects.all()
        project_id = projects.filter(project_name=project_name)[0]

        Models.objects.create(
            project_id=project_id,
            model_name=model_name,
            description=description
        )

        data = {
            "project_name": model_name,
            "description": description
        }

        return Response(status=201, data=data)

class CreateExperiment(APIView):
    def post(self, request):
        model_name = request.data.get("model_name", "")
        parameters = request.data.get("parameters", "")
        training_data_path = request.data.get("training_data_path", "")
        validation_data_path = request.data.get("validation_data_path", "")
        test_data_path = request.data.get("test_data_path", "")
        evaluation = request.data.get("evaluation", "")
        artifact_file_path = request.data.get("artifact_file_path", "")


        if not Models.objects.filter(model_name=model_name).exists():
            return Response(status=403, data={"msg": "존재하지 않는 모델명 입니다."})

        if Experiments.objects.filter(parameters=parameters).exists():
            return Response(status=403, data={"msg": "이미 존재하는 parameter입니다."})


        models = Models.objects.all()
        model_id = models.filter(model_name=model_name)[0]

        Experiments.objects.create(
            model_id=model_id,
            parameters=parameters,
            training_data_path=training_data_path,
            validation_data_path=validation_data_path,
            test_data_path=test_data_path,
            evaluation=evaluation,
            artifact_file_path=artifact_file_path
        )

        data = {
            "model_name": model_name,
            "parameters": parameters,
            "evaluation": evaluation,
            "artifact_file_path": artifact_file_path,
        }

        return Response(status=201, data=data)