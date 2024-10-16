from django.urls import path
from users.views import home_page

urlpatterns = [
    path('signup/', home_page)
]