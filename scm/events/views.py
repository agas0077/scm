import datetime as dt

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from events.models import EventMember, Event


@login_required()
def sign_up(request):
    response_data = {}
    if request.POST.get('action') == 'post':
        event_pk = int(request.POST.get('target_pk'))
        event = get_object_or_404(Event, pk=event_pk)
        member = request.user
        obj, created = EventMember.objects.get_or_create(
            event=event, member=member)

        response_data['btn_text'] = ('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Отмена'
                                     '&nbsp;&nbsp;&nbsp;&nbsp;')
        if not created:
            obj.delete()
            response_data['btn_text'] = 'Регистрация'

    return JsonResponse(response_data)


def index(request):
    template_name = 'events/index.html'
    events = Event.objects.order_by('-date')
    context = {
        'events': events,
        'now': dt.date.today(),
    }
    return render(request, template_name, context)


class Gallery(ListView):
    model = Event
    template_name = 'events/gallery.html'
    paginate_by = 10
    ordering = '-date'
