from django.contrib import admin

from polls.models import *

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(LongChoice)
admin.site.register(ChoicePoly)
admin.site.register(LongChoicePoly)