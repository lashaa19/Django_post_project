from django.contrib import admin
from .models import Post, Comment

class CommentsInline(admin.TabularInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('id', 'author', 'time_date', 'file')

    ordering = ('time_date',)

    list_editable = ('file',)

    readonly_fields = ('text', 'author', 'time_date')

    search_fields = ('text', 'author__username')

    list_filter = ('author', 'time_date')

    inlines = [CommentsInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('id', 'author', 'post', 'created_at',)

    readonly_fields = ('created_at', 'text', 'author', 'post')

    search_fields = ('text', 'author__username', )

    list_filter = ('author', 'created_at')

    fieldsets = (
        ("Content", {"fields": ("text", "file")}),
        ("Methadata", {"fields": ("author", "created_at")}),
    )




