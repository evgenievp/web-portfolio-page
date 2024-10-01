from django.urls import path


from web_page.main_page import views

urlpatterns = (
    path('', views.MainPage.as_view(), name='index page'),
    path('django-projects/', views.DjangoView.as_view(), name='django page'),
    path('data-structures-and-algos/', views.data_structures_view, name='data structures'),
    path('flask-projects/', views.flask_repos_view, name='flask page'),
    path('other-projects/', views.other_projects_view, name='other projects'),
    path('contacts/', views.ContactsPageView.as_view(), name='contacts page'),
    path('about/', views.AboutPageView.as_view(), name='about page'),

)
