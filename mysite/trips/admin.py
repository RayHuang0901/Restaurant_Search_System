from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from .models import Positions, Prices, Comment, Infos, Food_Type


@admin.register(Positions)
class PositionAdmin(ImportExportModelAdmin):
    list_display = ('Name', 'Area', 'Road', 'Door_num', 'Floor')
    

@admin.register(Prices)
class PositionAdmin(ImportExportModelAdmin):
    list_display = ('Name', 'Service_charge', 'min_charge', 'Avg_charge')

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('Name', 'CP', 'Service', 'Delicious_level', 'Clean')

@admin.register(Infos)
class Infodmin(ImportExportModelAdmin):
    list_display = ('Name', 'START_Time', 'Close_Time', 'Menu', 'FB', 'Phone')

@admin.register(Food_Type)
class FoodAdmin(ImportExportModelAdmin):
    list_display = ('Name', 'Type', 'Style', 'Veg')