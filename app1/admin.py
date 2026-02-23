from django.contrib import admin
from .models import book


# Register your models here.
# class BookAdmin(admin.ModelAdmin):
#     list_display=('title','author','price','pub_date')
#     list_filter=('author',)
#     search_fields=('title','author',)
#     ordering=('pub_date',)
#     list_editable=('price',)


class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','price','pub_date')
    actions=['Mark_Free']
    def Mark_Free(self,request,queryset):
        queryset.update(price=0)
        self.message_user(request,"selected books have been marked as free.")
    Mark_Free.short_description="Mark selected books as free"
admin.site.register(book, BookAdmin)
