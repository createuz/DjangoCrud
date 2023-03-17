from django.urls import path
from apps.views import homepage, add_person

urlpatterns = [
    path('', homepage, name='homepage'),
    # path('add_person', add_person, name='add'),
]