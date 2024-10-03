from django.views import generic as views
from django.shortcuts import render


class MainPage(views.TemplateView):
    template_name = 'index.html'


class DjangoView(views.TemplateView):
    template_name = 'django_projects.html'


def data_structures_view(request):
    return render(request, 'data_structures_and_algos.html')


def flask_repos_view(request):
    return render(request, 'flask_repos.html')


def other_projects_view(request):
    return render(request, 'other_projects.html')


class ContactsPageView(views.TemplateView):
    template_name = 'contacts.html'


class AboutPageView(views.TemplateView):
    template_name = 'about.html'


