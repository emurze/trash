from django.urls import path

from .views import TerminalView

app_name = 'terminal'

urlpatterns = [
    path('', TerminalView.as_view(), name='terminal'),
]