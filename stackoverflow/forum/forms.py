from django import forms
from forum.models import Question, Answer

class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'title',
            'text',
            'user',
        ]

class AnswerCreateForm(forms.ModelForm):
    class Meta:
        model = Answer
        fiels = [
            'text'
        ]