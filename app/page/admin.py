from django.contrib import admin
from page import models


@admin.register((models.PageContent))
class ShareAdmin(admin.ModelAdmin):
    pass
