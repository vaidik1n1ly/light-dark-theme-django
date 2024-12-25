from django.urls import path
from .views import ThemeSettingView, index

urlpatterns = [
    path('', index, name="index"),
    path('api/theme/', ThemeSettingView.as_view(), name='theme-setting'),
]