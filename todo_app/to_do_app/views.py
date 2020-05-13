from django.shortcuts import render
from . import models
from django.views.generic import DeleteView
# Create your views here.

def home(request):
    todo_item = request.POST.get('todo_item')
    if todo_item:
        record = models.Todo(text=todo_item)
        record.save()
    all_tasks = models.Todo.objects.all().order_by('-created')
    data_for_front_end = {
        'items' : all_tasks
    }
    return render(request, "home.html", data_for_front_end)


class PostDelete(DeleteView):
    model = models.Todo
    success_url = '/'