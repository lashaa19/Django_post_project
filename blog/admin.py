from django.contrib import admin
from .models import Post

#@admin.register(Post)
#class postadmin(admin.ModelAdmin):
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('id', 'author', 'time_date', 'file')

    readonly_fields = ('text', 'author', 'time_date')

    search_fields = ('text', 'author__username')

    list_filter = ('author',)



#admin.site.register(Post, PostAdmin)


