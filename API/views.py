from django.shortcuts import render
from django.http import JsonResponse
from Models.models import Student
from django.views.decorators.csrf import csrf_exempt
import json 

# Create your views here.


def get_students(request):
    students = Student.objects.all()    
    data = list(students.values())
    return JsonResponse(data, safe=False)

def get_student(request, student_number):
    student = Student.objects.get(student_number=student_number)
    data = {
        'name': student.name,
        'student_number': student.student_number,
        'email': student.email,
        'phone_number': student.phone_number,
        'address': student.address,
        'course_status': student.course_status,
        'curriculum_year': student.curriculum_year
    }
    return JsonResponse(data)

@csrf_exempt
def set_curriculum_status(request):
    if request.method == 'POST':
        data = request.body
        data = data.decode('utf-8') 
        json_data = json.loads(data) 
        student = Student.objects.get(id=json_data['student_id']) 
        student.course_status = json_data['status'] 
        student.curriculum_year = json_data['curriculum_year']
        student.save()
        print(data) 
        return JsonResponse({'message': 'success'})