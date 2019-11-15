from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

# Create
# user가 입력하는 창(html)
def new(request):
    return render(request, 'workshop19/new.html')
    
# user가 넘긴 데이터를 실제 DB에 저장하는 액션
# @csrf_exempt -> csrf 방어를 해제
def create(request):
    input_name = request.POST.get('input_name')
    input_email = request.POST.get('input_email')
    input_birthday = request.POST.get('input_birthday')
    input_age = request.POST.get('input_age')
    
    student = Student(name=input_name, email=input_email, birthday=input_birthday, age=input_age)
    student.save()
    # return HttpResponse(200)
    return redirect(f'/workshop19/students/{student.id}')
    
# Read
# 목록을 보여주는 함수
def index(request):
    students = Student.objects.all()
    return render(request, 'workshop19/index.html', { 'students': students })
    
def detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'workshop19/detail.html', { 'student': student })
    
# Update
def update_student(request, id):
    student = Student.objects.get(id=id) # if랑 else 코드 반복되서 밖으로 빼줌
    # HTML 보여주기
    if request.method == 'GET':
        birthday = student.birthday.strftime('%Y-%m-%d')
        return render(request, 'workshop19/edit.html', {'student': student, 'birthday': birthday})
    
    #수정하기    
    else:
        student.name = request.POST.get('input_name')
        student.email = request.POST.get('input_email')
        student.birthday = request.POST.get('input_birthday')
        student.age = request.POST.get('input_age')
        student.save()
        return redirect(f'/workshop19/students/{student.id}/')
        
# Destory
# 특정 student을 삭제하는 액션
def delete(request, id):
    # Post 요청일 때는, 삭제, redircet
    if request.method == 'POST':
        student = Student.objects.get(id=id) # 앞에 있는 id
        student.delete()
        return redirect ('/workshop19/students/')
    # 그 외는 삭제하지 않음
    else:
        return redirect(f'/workshop19/students/{id}/')

