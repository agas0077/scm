from django.urls import path

from mentor.views import (MentorView, MenteeView,
                          become_mentor, become_mentee,
                          sign_up)

app_name = 'mentor'

urlpatterns = [
    path('mentor/', MentorView.as_view(), name='mentor_index'),
    path('mentee/', MenteeView.as_view(), name='mentee_index'),
    path('become_mentor/', become_mentor, name='become_mentor'),
    path('become_mentee/', become_mentee, name='become_mentee'),
    path('sign_up/', sign_up, name='sign_up'),
]
