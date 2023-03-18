from django.urls import path
from . import views

app_name="acconut"
urlpatterns = [
    path("profile/<int:pk>", views.ProfileDetailView.as_view(), name="profile"),
    path("register_user/",views.register_user, name="register_user"),
    path("login_user/",views.login_user, name="login"),


]
