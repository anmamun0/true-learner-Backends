from django.contrib import admin

# Register your models here.
from .models import Course, Video, Category
admin.site.register(Course)
admin.site.register(Video)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)