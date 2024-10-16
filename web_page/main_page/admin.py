from django.contrib import admin


from web_page.main_page.models import ApplicationModel, AboutMeModel

from web_page.main_page.models import UserAccount


@admin.register(ApplicationModel)
class Applications(admin.ModelAdmin):
    pass


@admin.register(AboutMeModel)
class AboutMe(admin.ModelAdmin):
    pass


@admin.register(UserAccount)
class UserAccount(admin.ModelAdmin):
    pass