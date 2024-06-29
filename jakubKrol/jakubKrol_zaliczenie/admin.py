from django.contrib import admin
from .models import Article

# Register your models here.
# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')
    list_filter = ('author', 'year')
    search_fields = ('title', 'description', 'author')
    date_hierarchy = 'date'
    ordering = ('date',)
    fields = ('title', 'description', 'body', 'date', 'author', 'year', 'image')
    readonly_fields = ('date',)
    pass

