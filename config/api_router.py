from django.urls import include, path

urlpatterns = [
    path("users/", include("hapvic.users.api.urls")),
]

app_name = "api"
