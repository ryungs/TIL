from mton.models import Student, Lecture, Enrollment


create_student = Student.objects.create
s1 = create_student(name='곽동령')
s2 = create_student(name='이유림')
s3 = create_student(name='안도건')

l1 = Lecture.objects.create(title='알고리즘')
l2 = Lecture.objects.create(title='장고')

Enrollment.objects.create(lecture=l1, student=s1)
Enrollment.objects.create(lecture=l1, student=s2)
Enrollment.objects.create(lecture=l1, student=s3)

곽동령 = Student.objects.get(id=1)
곽동령_수강신청_목록 = 곽동령.enrollment_set.all()
for 수강신청 in 곽동령_수강신청_목록:
    print(수강신청.lecture.title)

# id = 1 lecture_id = 1, student_id = 1
# id = 1 lecture_id = 2, student_id = 1
