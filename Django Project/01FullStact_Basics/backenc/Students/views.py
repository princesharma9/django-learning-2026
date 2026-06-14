from django.shortcuts import render
from Students.models import student
from django.http import JsonResponse
# Create your views here.
def student_detail(request, id):
    data = student.objects.filter(id=id).values().first()
    return JsonResponse(data, safe=False)


def stu_List(request):
    stu_profile_data = list(student.objects.all().values())
    return JsonResponse(stu_profile_data, safe=False)