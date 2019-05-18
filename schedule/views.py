from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Schedule
from .forms import ScheduleForm

def index(request):
    schedule_list = Schedule.objects.order_by('id')

    form = ScheduleForm()

    context = {'schedule_list' : schedule_list, 'form' : form}

    return render(request, 'schedule/index.html', context)

@require_POST
def add_schedule(request):
    form = ScheduleForm(request.POST)

    if form.is_valid():
        new_schedule = Schedule(text=request.POST['text'])
        new_schedule.save()

    return redirect('index')

def complete_schedule(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    schedule.complete = True
    schedule.save()

    return redirect('index')

def delete_completed(request):
    Schedule.objects.filter(complete__exact=True).delete()

    return redirect('index')

def delete_all(request):
    Schedule.objects.all().delete()

    return redirect('index')