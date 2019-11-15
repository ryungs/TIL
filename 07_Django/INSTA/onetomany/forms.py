from django import forms
from .models import Writer, Book, Chapter

# Writer, Book, Chapter

class WriterModelForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = '__all__' # 전체를 불러 오는 거

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class ChapterModelFrom(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'

