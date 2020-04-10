from django.contrib import admin
from elements.models import (
    Column, PostIt, Board, BoardColumn)


class PostItAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'column']
    list_filter = ('column', 'column__board__ceremony__title')


admin.site.register(Column)
admin.site.register(PostIt, PostItAdmin)
admin.site.register(Board)
admin.site.register(BoardColumn)
