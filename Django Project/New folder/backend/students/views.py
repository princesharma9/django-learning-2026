from django.shortcuts import render
from django.http import JsonResponse

# from backend.students.models import Students
from .models import Students
# from .models import Students
# Create your views here.
def students(request):
    students_list = list(Students.objects.all().values())
    # print(students_list)
    # students_list = {
    #     'name': 'John Doe',
    #     'age': 20,
    #     'grade': 'A'
    # }
    return JsonResponse(students_list, safe=False)


