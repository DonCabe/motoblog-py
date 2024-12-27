from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'total_likes')
    search_fields = ('title', 'description')
    list_filter = ('publication_date',)