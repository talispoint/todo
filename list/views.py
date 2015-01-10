from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

from list.models import Todo

# Create your views here. 

class IndexView(generic.ListView):
	template_name = "list/index.html"
	context_object_name = "todo_list"

	def get_queryset(self):
		return Todo.objects.all()

# def index(request):
# 	todo_list = Todo.objects.all()
# 	context = {
# 		"todo_list": todo_list
# 	}
# 	return render(request, "list/index.html", context)

class DetailView(generic.DetailView):
	model = Todo
	template_name = "list/detail.html"

# def detail(request, todo_id):
# 	todo = get_object_or_404(Todo, pk=todo_id)
# 	context = {"todo": todo}
# 	return render(request, "list/detail.html", context)

def finished(request, todo_id):
	todo = get_object_or_404(Todo, pk=todo_id)
	try:
		todo.finished = True if request.POST['finished'] else False
	except:
		todo.finished = False
	todo.save()
	return HttpResponseRedirect(reverse("list:index"))