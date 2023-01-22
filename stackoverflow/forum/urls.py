from django.urls import path
from forum.views import HomeView, QuestionDetailView, create_question_views, create_answer_views

app_name = 'forum'

urlpatterns = [
    path('', HomeView.as_view(), name ='home'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('ask/', create_question_views, name='question-add'),
    path('question-answer/int:pk/', create_answer_views, name = 'answer-add')
    
]
