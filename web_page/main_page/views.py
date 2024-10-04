from django.views import generic as views
from django.shortcuts import render
from web_page.main_page.forms import Project


class MainPage(views.TemplateView):
    template_name = 'index.html'


def django_page_view(request):
    form = Project
    context = {
        'forms': form,
    }

    return render(request, 'django_projects.html', context=context)


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


