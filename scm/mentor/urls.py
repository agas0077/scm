from django.urls import path

from mentor.views import (MentorView, MenteeView,
                          become_mentor, become_mentee,
                          SignUpMeneeView, SignUpMentorView, sign_up_success)

app_name = 'mentor'

urlpatterns = [
    path('mentor/', MentorView.as_view(), name='mentor_index'),
    path('mentee/', MenteeView.as_view(), name='mentee_index'),

    # Стать ментором у менти или стать менти у ментора
    path('mentor/become/', become_mentor, name='become_mentor'),
    path('mentee/become/', become_mentee, name='become_mentee'),

    # Регистрация в менторской программе
    path('sign_up/mentor', SignUpMentorView.as_view(), name='sign_up_mentor'),
    path('sign_up/mentee', SignUpMeneeView.as_view(), name='sign_up_mentee'),
    path('sign_up/success', sign_up_success, name='sign_up_success'),
]
