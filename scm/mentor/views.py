from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView


from mentor.models import Mentor, Mentee, MentorMentee

Member = get_user_model()

APPLICTION_SUBMITED = 'Отменить заявку'
APPLICTION_CAN_BE_SUBMITED = 'Подать заявку'

MENTOR_MAIL_SUBJECT = 'Менторская программа'


def _become(request, mentor, mentee):
    response_data = {}
    if request.POST.get('action') == 'post':
        obj, created = MentorMentee.objects.get_or_create(
            mentor=mentor, mentee=mentee)

        mail_subject = ' '.join(
            [MENTOR_MAIL_SUBJECT, ': новая заявка'])
        mail_message = ('Получена новая заявка на менторство:\n'
                        f'Ментор: {mentor} - {mentor.member.email}\n'
                        f'Менти: {mentee} - {mentee.member.email}\n')

        response_data['btn_text'] = APPLICTION_SUBMITED
        if not created:
            obj.delete()
            mail_subject = ' '.join(
                [MENTOR_MAIL_SUBJECT, ': отмена заявки'])
            mail_message = ('Оменена заявка на менторство:\n'
                            f'Ментор: {mentor} - {mentor.member.email}\n'
                            f'Менти: {mentee} - {mentee.member.email}\n')
            response_data['btn_text'] = APPLICTION_CAN_BE_SUBMITED

    send_mail(mail_subject,
              mail_message,
              settings.DEFAULT_FROM_EMAIL,
              [email for name, email in settings.ADMINS],
              True)

    return JsonResponse(response_data)


class MentorView(LoginRequiredMixin, ListView):
    model = Mentee
    template_name = 'mentor/mentor_index.html'

    def get_queryset(self):
        queryset = Mentee.objects.exclude(member=self.request.user)
        queryset = queryset.filter(approved=True)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        chosen_mentee = self.request.user.mentor
        if hasattr(chosen_mentee, 'mentor_mentee_mentor'):
            ctx['chosen'] = chosen_mentee.mentor_mentee_mentor.mentee

        ctx['APPLICTION_SUBMITED'] = APPLICTION_SUBMITED
        ctx['APPLICTION_CAN_BE_SUBMITED'] = APPLICTION_CAN_BE_SUBMITED

        return ctx


class MenteeView(LoginRequiredMixin, ListView):
    model = Mentor
    queryset = Mentor.objects.all()
    template_name = 'mentor/mentee_index.html'

    def get_queryset(self):
        queryset = Mentor.objects.exclude(member=self.request.user)
        queryset = queryset.filter(approved=True)
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        chosen_mentor = self.request.user.mentee
        if hasattr(chosen_mentor, 'mentor_mentee_mentee'):
            ctx['chosen'] = chosen_mentor.mentor_mentee_mentee.mentor

        ctx['APPLICTION_SUBMITED'] = APPLICTION_SUBMITED
        ctx['APPLICTION_CAN_BE_SUBMITED'] = APPLICTION_CAN_BE_SUBMITED

        return ctx


@login_required()
def become_mentor(request):
    mentor = request.user.mentor
    mentee_pk = int(request.POST.get('target_pk'))
    mentee = get_object_or_404(Mentee, pk=mentee_pk)
    return _become(request, mentor, mentee)


@login_required()
def become_mentee(request):
    mentee = request.user.mentee
    mentor_pk = int(request.POST.get('target_pk'))
    mentor = get_object_or_404(Mentor, pk=mentor_pk)
    return _become(request, mentor, mentee)


def sign_up(request):
    response_data = {}
    template_name = 'mentor/sign_up.html'
    member = request.user
    who = request.POST.get('target_pk')
    if request.POST.get('action') == 'post':
        if who == 'mentor':
            mail_subject = ' '.join(
                [MENTOR_MAIL_SUBJECT, ': новый ментор'])
            mail_message = ('Новый участник хочет стать ментором:\n'
                            f'Ментор: {member.email}')
        elif who == 'mentee':
            mail_subject = ' '.join(
                [MENTOR_MAIL_SUBJECT, ': новый менти'])
            mail_message = ('Новый участник хочет стать менти:\n'
                            f'Ментор: {member.email}')

        send_mail(mail_subject,
                  mail_message,
                  settings.DEFAULT_FROM_EMAIL,
                  [email for name, email in settings.ADMINS],
                  True)
        
        response_data['btn_text'] = 'Заявка отправлена'

        return JsonResponse(response_data)
    return render(request, template_name)
