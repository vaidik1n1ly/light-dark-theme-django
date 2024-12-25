from django.contrib.auth.models import User
from django.apps import apps

def create_default_user_and_setting(sender, **kwargs):
    Setting = apps.get_model('base', 'Setting')
    user, created = User.objects.get_or_create(username='user', defaults={'password': 'P@ssw0rd'})
    Setting.objects.get_or_create(user=user, name='theme', defaults={'value': 'light'})