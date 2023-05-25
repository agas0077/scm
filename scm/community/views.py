import datetime as dt

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from events.models import Event
from members.forms import MemberForm
from members.models import DATE_FIELDS, Member
from news.models import News


User = get_user_model()
DATE_FROMAT = '%Y-%m-%d'


def _convert_date(request_copy):
    '''
    Получает на вход копию POST запроса.
    Возвращает datetime.
    Необходимо, так как html возвращает именно строку,
    которую не сохранить в БД.
    '''
    for field in DATE_FIELDS:
        try:
            if isinstance(request_copy[field], str):
                request_copy[field] = dt.datetime.strptime(
                    request_copy[field], DATE_FROMAT)
        except KeyError:
            pass
        except ValueError:
            pass
    return request_copy


def index(request):
    events = Event.objects.order_by('date')
    members = Member.objects.all()
    news = News.objects.order_by('date', '-pk')[:3]

    subscription_form = MemberForm(
        request.POST or None,
        files=request.FILES or None)
    template = 'index.html'
    context = {
        'subscription_form': subscription_form,
        'events': events,
        'news': news,
        'members': members,
        'mentors_count': None,  # TODO: Добавть количество менторов
    }

    if not request.method == "POST":
        return render(request, template, context)

    subscription = request.POST.copy()
    subscription = _convert_date(subscription)
    subscription['password'] = User.objects.make_random_password()
    subscription_form = MemberForm(subscription or None)
    context['form'] = subscription_form

    if not subscription_form.is_valid():
        return render(request, template, context)

    subscription_form.save()
    return redirect('members:sign_up_success')


def create_project(request):
    '''Вью-функция создания проекта.'''