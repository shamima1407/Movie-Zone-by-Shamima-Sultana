from django.contrib import admin
from .models import Movie, Banner_Movie
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.

@admin.register(Movie, Banner_Movie)
class moviedata(ImportExportActionModelAdmin):
    pass

