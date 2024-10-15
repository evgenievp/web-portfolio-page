from django.urls import path
from web_page.main_page import views
from django.conf.urls.static import static
from django.conf import settings

handler404 = 'django.views.defaults page_not_found'


urlpatterns = [
    path('', views.MainPage.as_view(), name='index page'),
    path('django-projects/', views.django_page_view, name='django page'),
    path('data-structures-and-algos/', views.data_structures_view, name='data structures'),
    path('flask-projects/', views.flask_repos_view, name='flask page'),
    path('other-projects/', views.other_projects_view, name='other projects'),
    path('contacts/', views.ContactsPageView.as_view(), name='contacts page'),
    path('about/', views.AboutPageView.as_view(), name='about page'),
    path('display-project/<int:pk>/', views.display_project, name='display project'),
    path('login/', views.LoginView.as_view(), name='login page'),
    path('register/', views.RegisterPage.as_view(), name='register page'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

