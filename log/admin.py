from django.contrib import admin
from .models import Push, Sms, User, File, Spnavigator, Lk, Project

admin.site.register(Push)
admin.site.register(Sms)
admin.site.register(Spnavigator)
admin.site.register(Lk)
admin.site.register(User)
admin.site.register(File)
admin.site.register(Project)
