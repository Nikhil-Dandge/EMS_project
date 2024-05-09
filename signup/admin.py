from django.contrib import admin
from signup.models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display=('username','password')


admin.site.register(Signup,SignupAdmin)
