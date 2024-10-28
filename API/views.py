from django.http import JsonResponse
from Models.models import Student, Curriculum, ProgramHighlight, Article, Account
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, Case, When, IntegerField
from django.shortcuts import get_object_or_404
from django.contrib.auth import login as login_user, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
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

def get_program_data(request):
    program = request.GET.get('program', None)
    
    if program:
        students = Student.objects.filter(program=program)
    else:
        students = Student.objects.all()
    
    students = students.values('program').annotate(
        enrolled=Count(Case(When(student_status='Enrolled', then=1), output_field=IntegerField())),
        graduated=Count(Case(When(student_status='Graduated', then=1), output_field=IntegerField())),
        failed=Count(Case(When(student_status='Failed', then=1), output_field=IntegerField())),
        incomplete=Count(Case(When(student_status='Incomplete', then=1), output_field=IntegerField())),
        number_of_students=Count('id')
    )
    
    data = {student['program']: {
                'enrolled': student['enrolled'],
                'graduated': student['graduated'],
                'failed': student['failed'],
                'incomplete': student['incomplete'], 
                'number_of_students': student['number_of_students']
            } for student in students}
    
    return JsonResponse(data)

def get_yearly_performance(request):
    program = request.GET.get('program', None)
    performance_data = []

    # Get all curriculum years for the program
    curriculum_years = Student.objects.filter(program=program).values_list('curriculum_year', flat=True).distinct()

    for year in curriculum_years:
        # Get all students for the program and curriculum year
        students = Student.objects.filter(program=program, curriculum_year=year) 
        students = students.values('program').annotate(
        enrolled=Count(Case(When(student_status='Enrolled', then=1), output_field=IntegerField())),
        graduated=Count(Case(When(student_status='Graduated', then=1), output_field=IntegerField())),
        failed=Count(Case(When(student_status='Failed', then=1), output_field=IntegerField())),
        incomplete=Count(Case(When(student_status='Incomplete', then=1), output_field=IntegerField())),
        number_of_students=Count('id')
    )

        total_students = students[0]['number_of_students']
        pass_rate = students[0]['graduated'] / total_students * 100
        fail_rate = students[0]['failed'] / total_students * 100
        enrolled_rate = students[0]['enrolled'] / total_students * 100
        incomplete_rate = students[0]['incomplete'] / total_students * 100
        


        performance_data.append({
            'year': year,
            'total_students': total_students,
            'pass_rate': pass_rate,
            'fail_rate': fail_rate,
            'enrolled_rate': enrolled_rate,
            'incomplete_rate': incomplete_rate,
        })
    

    return JsonResponse(performance_data, safe=False)

def get_curriculum(request):
    curriculum = Curriculum.objects.filter(program='BSIT').order_by('year')
    data = [] 
    for c in curriculum:
        data.append({
            'year': c.year,
            'data': c.data
    })
        
    return JsonResponse(data, safe=False)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
    

def get_program_highlights(request):
    program = request.GET.get('program')
    department = request.GET.get('department')
    
    filters = {}
    if program:
        filters['program'] = program
    if department:
        filters['department'] = department
        
    print(filters)
    
    program_highlights = ProgramHighlight.objects.filter(**filters).values('title', 'content', 'image')
    
    data = list(program_highlights)

    return JsonResponse(data, safe=False)


def get_program_articles(request):
    program = request.GET.get('program')
    department = request.GET.get('department')
    category = request.GET.get('category')
    
    filters = {}
    if program:
        filters['program'] = program
    if department:
        filters['department'] = department
    if category and category != 'all':
        filters['category'] = category
    
    articles = Article.objects.filter(**filters).order_by('-date')
    
    data = [{
        'id': article.pk,
        'title': article.title,
        'content': article.content,
        'image': article.image.url if article.image else None,
        'author': f"{article.author.first_name} {article.author.last_name}",
        'category': article.category,
        'date': article.date,
    } for article in articles]
    
    return JsonResponse(data, safe=False)

def get_article(request):
    article_id = request.GET.get('id', None)
    article = get_object_or_404(Article, id=article_id)
    data = {
        'title': article.title,
        'content': article.content,
        'image': article.image.url,
        'author': article.author.first_name + ' ' + article.author.last_name,
        'category': article.category,
        'date': article.date,
    }
    return JsonResponse(data)

@csrf_exempt    
def verify_account(request):
    if request.method == 'POST':
        data = request.body 
        data = data.decode('utf-8') 
        json_data = json.loads(data) 
        username = json_data['username'] 
        password = json_data['password']
        account = authenticate(username=username, password=password)
        
        if account:
            login_user(request, account)
            refresh = RefreshToken.for_user(account)
            
            return JsonResponse({'status': 'success',
                                 'role': account.role,
                                 'refresh': str(refresh),
                                 'access': str(refresh.access_token)})
        else:
            return JsonResponse({'status': 'failed'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def verify_auth(request): 
    if request.user and request.user.is_authenticated:
        data = {
            'firstname': request.user.first_name,
            'lastname': request.user.last_name,
            'role': request.user.role,
            'program': request.user.program,
            'department': request.user.department,
            'email': request.user.email
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'status': 'unauthorized'})
