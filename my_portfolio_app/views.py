from django.shortcuts import render
from .models import Project,Contact,Skill
from django.views.generic import ListView,CreateView
from django.core.paginator import Paginator
from .forms import ContactForm
from django.urls import reverse_lazy

def home(request):
    return render(request,'hero.html')

def list_projects(request):
    category = request.GET.get('category', 'all')
    print(category)
    if category == 'all':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(category__name__icontains = category ).distinct()
    
    paginator = Paginator(projects,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    print(page_obj.object_list)
    return render(request,'projects.html',{"object_list":page_obj,"category":category})

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact')

def about(request):
    skills = Skill.objects.all()
    
    return render(request,'about.html',{"skills":skills})