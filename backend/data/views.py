from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .models import Doctor, User, Test, Question, Result


class DoctorsView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        return Response({"doctors": doctors})


class UsersView(APIView):
    def get(self, request):
        doctor_id = request.GET.get("doctor_id", None)
        if not doctor_id:
            users = User.objects.all()
        else:
            doctor = get_object_or_404(Doctor, id=doctor_id)[0]
            users = get_object_or_404(User, doctor=doctor).all()
        return Response({"users": users})


class TestView(APIView):
    def get(self, request):
        test_id = request.GET.get("test_id", None)
        if not test_id:
            tests = Test.objects.all()
            return {"tests": tests}
        test = get_object_or_404(Test, id=test_id)[0]
        with_questions = request.GET.get("with_questions", False)
        if with_questions:
            questions = get_object_or_404(Question, test=test).all()
            return Response({"test": test, "questions": questions})
        return Response({"test": test})


class ResultView(APIView):
    def get(self, request):
        user_id = request.GET.get("user_id", None)
        test_id = request.GET.get("test_id", None)
        user = get_object_or_404(User, id=user_id)
        test = get_object_or_404(Test, id=test_id)
        results = get_object_or_404(Result, user=user, test=test).all()
        return Response({"results": results})

# TODO: SERIALIZERS!
