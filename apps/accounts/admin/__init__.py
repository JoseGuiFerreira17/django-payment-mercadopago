from django.contrib.admin import site
from apps.accounts.admin.user import UserAdmin
from apps.accounts.models import User


site.register(User, UserAdmin)
