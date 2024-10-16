from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from django.db.models import F
from django.contrib.auth import views as auth_views


import web_page
from web_page.main_page.forms import Project, RegisterForm, LoginForm
from web_page.main_page.models import ApplicationModel, AboutMeModel, UserAccount


class MainPage(views.TemplateView):
    template_name = 'index.html'


class LoginPage(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login_page.html'
    next_page = reverse_lazy('index page')


class RegisterPage(views.CreateView):
    template_name = 'register_page.html'
    model = UserAccount
    form_class = RegisterForm
    success_url = 'index.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect('index page')


def django_page_view(request):
    apps = ApplicationModel.objects.all().filter(type_of_application__exact='Django Apps')
    form = Project(request.POST or request.GET)
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
    form = Project(request.POST or request.GET)
    context = {
        'apps': apps,
        'form': form,
    }
    return render(request, 'data_structures_and_algos.html', context=context)


def flask_repos_view(request):
    apps = ApplicationModel.objects.all().filter(type_of_application__exact='Flask Apps')
    form = Project(request.POST or request.GET)
    context = {
        'apps': apps,
        'form': form,
    }
    return render(request, 'flask_repos.html', context=context)


def other_projects_view(request):
    apps = ApplicationModel.objects.all().filter(type_of_application__exact='Other')
    form = Project(request.POST or request.GET)
    context = {
        'apps': apps,
        'form': form,
    }
    return render(request, 'other_projects.html', context=context)


class ContactsPageView(views.TemplateView):
    template_name = 'contacts.html'


class AboutPageView(views.DetailView):
    model = AboutMeModel
    template_name = 'about.html'
    context_object_name = 'model'

    def get_object(self):
        return AboutMeModel.objects.first()


class UserSignOut(auth_views.LogoutView):
    next_page = reverse_lazy('index page')
