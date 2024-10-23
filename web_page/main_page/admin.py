from django.contrib import admin
from web_page.main_page.models import ApplicationModel, AboutMeModel, User, Message


@admin.register(ApplicationModel)
class Applications(admin.ModelAdmin):
    pass


@admin.register(AboutMeModel)
class AboutMe(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAccount(admin.ModelAdmin):
   pass


@admin.register(Message)
class Message(admin.ModelAdmin):
    pass
