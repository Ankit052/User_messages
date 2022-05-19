from .models import Message
from django.contrib import admin

# Register your models here.


class MessageAdmin(admin.ModelAdmin):
    list_display = ["message"]


admin.site.register(Message,MessageAdmin)