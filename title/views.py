from django.views.generic import ListView
from django.views.generic.edit import CreateView
from title.models import Title
# Create your views here.

# http://localhost:8000/titles


# def index(request):
#    return HttpResponse("test")


class TitleListView(ListView):
    model = Title
    template_name = "TitleList.html"


class TitleCreateView(CreateView):
    CreateView.model = Title
    fields = ['name']
    template_name = "TitleCreate.html"
