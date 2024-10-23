from django.urls import path
from web_page.main_page import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import re_path

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
    path('login/', views.LoginPage.as_view(), name='login page'),
    path('register/', views.register_page, name='register page'),
    path('signout/', views.UserSignOut.as_view(), name='sign out'),
    path('write_me/', views.WriteMeView.as_view(), name='write me'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
