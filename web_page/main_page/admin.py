from django.contrib import admin


from web_page.main_page.models import ApplicationModel, AboutMeModel


@admin.register(ApplicationModel)
class Applications(admin.ModelAdmin):
    pass


@admin.register(AboutMeModel)
class AboutMe(admin.ModelAdmin):
    pass