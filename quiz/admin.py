from django.contrib import admin
from .models import Quiz, Submission, UserInfo

# Register your models here.
admin.site.register(Quiz)
admin.site.register(Submission)
admin.site.register(UserInfo)