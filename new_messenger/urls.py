from django.urls import path, include
from new_messenger.views import Authentication


urlpatterns = [
    path('authentication/', view=Authentication.as_view())
]


