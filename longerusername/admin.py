from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from longerusername.forms import UserCreationForm, UserChangeForm

class LongerUserNameUserAdminMixin(object):
    add_form = UserCreationForm
    form = UserChangeForm
    

if get_user_model() == User:
    class LongerUserNameUserAdmin(LongerUserNameUserAdminMixin, UserAdmin):
        pass

    admin.site.unregister(User)
    admin.site.register(User, LongerUserNameUserAdmin)
