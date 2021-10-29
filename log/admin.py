from django.contrib import admin
from .models import Push, Sms, User, File, Spnavigator, Lk

admin.site.register(Push)
admin.site.register(Sms)
admin.site.register(Spnavigator)
admin.site.register(Lk)
admin.site.register(User)
admin.site.register(File)
