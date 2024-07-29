from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display="Title","Description","Duedate","Priority","Status",

admin.site.register(Member)
