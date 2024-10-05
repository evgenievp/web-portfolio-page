from django.contrib import admin


from web_page.main_page.models import ApplicationModel


@admin.register(ApplicationModel)
class Applications(admin.ModelAdmin):
    pass
