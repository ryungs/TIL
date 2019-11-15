from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel

class MagazineArticle(TitleDescriptionModel, TimeStampedModel):
    content = models.TextField()


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # 이말을 쓰면 table에 반영 안된다
    class Meta:
        abstract = True

class Writer(TimeStamp):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Book(TimeStamp):
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, default='', unique=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.id}: {self.author}: {self.title}'

class Chapter(TitleDescriptionModel, TimeStampedModel):
    # title, description, created, modified
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.book}'


#----------------------------------------------------------------------------------

class Student(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return f'{self.id}: {self.name}'

class Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}: {self.student}, {self.student}'

class Reply(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    content = models.CharField(max_length=30)

