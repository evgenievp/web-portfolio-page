from django.views import generic as views
from django.shortcuts import render, redirect
from django.db.models import F

import web_page
from web_page.main_page.forms import Project
from web_page.main_page.models import ApplicationModel, AboutMeModel


class MainPage(views.TemplateView):
    template_name = 'index.html'


def django_page_view(request):
    apps = ApplicationModel.objects.all().filter(type_of_application__exact='Django Apps')
    form = Project(request.POST)
    context = {
        'apps': apps,
        'form': form,
    }

    return render(request, 'django_projects.html', context=context)


def display_project(request, pk):

    item = ApplicationModel.objects.get(pk=pk)
    context = {
        'item': item,
    }

    if request.POST.get('vote') == 'like':
        item.all_votes = F('all_votes') + 1
        item.save()
        item.refresh_from_db()
        return redirect('index page')
    elif request.POST.get('vote') == 'dislike':
        item.all_votes = F('all_votes') - 1
        item.save()
        item.refresh_from_db()
        return redirect('index page')

    return render(request, 'display_project_page.html', context=context)


def data_structures_view(request):
    apps = ApplicationModel.objects.all().filter(type_of_application__exact='Data Structures')
    form = Project(request.POST)
    context = {
        'apps': apps,
        'form': form,
    }
    return render(request, 'data_structures_and_algos.html', context=context)


def flask_repos_view(request):
    apps = ApplicationModel.objects.all().filter(type_of_application__exact='Flask Apps')
    form = Project(request.POST)
    context = {
        'apps': apps,
        'form': form,
    }
    return render(request, 'flask_repos.html', context=context)


def other_projects_view(request):
    apps = ApplicationModel.objects.all().filter(type_of_application__exact='Other')
    form = Project(request.POST)
    context = {
        'apps': apps,
        'form': form,
    }
    return render(request, 'other_projects.html')


class ContactsPageView(views.TemplateView):
    template_name = 'contacts.html'


class AboutPageView(views.DetailView):
    model = AboutMeModel
    template_name = 'about.html'
    context_object_name = 'model'

    def get_object(self):
        return AboutMeModel.objects.first()