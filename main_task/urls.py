from django.urls import path
from .views import AllUsersView

app_name = "main_task"

urlpatterns = [
    path("users/", AllUsersView.as_view(), name="all_users")
]
