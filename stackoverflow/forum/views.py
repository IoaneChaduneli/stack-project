from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from forum.models import Question
from forum.forms import QuestionCreateForm
# Create your views here.

class HomeView(ListView):
    model = Question
    template_name = 'forum/question_list.html'

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'forum/question_detail.html'


def create_question_views(request):
    if request.method == 'GET':
        return render (
                request, 
                'forum/question_add.html',
            {
                'form' : QuestionCreateForm(),
            })
    else:
        form = QuestionCreateForm(request.POST)

        if form.is_valid:
            form.save()
            return redirect('forum:home')

        return render (
                request, 
                'forum/question_add.html',
            {
                'form' : form,
            })
        