from django.urls import path
from django.views.generic import RedirectView

from .views import (
    upload_document,
    chat,
    signup_view,
    conversation,
    logout_view,
    CustomLoginView,
    admin_dashboard,
    delete_document,
)

urlpatterns = [

    path(
        "",
        RedirectView.as_view(pattern_name="login"),
        name="home",
    ),

    path(
        "login/",
        CustomLoginView.as_view(),
        name="login",
    ),

    path(
        "logout/",
        logout_view,
        name="logout",
    ),

    path(
        "signup/",
        signup_view,
        name="signup",
    ),

    path(
        "admin-dashboard/",
        admin_dashboard,
        name="admin_dashboard",
    ),

    path(
        "upload/",
        upload_document,
        name="upload_document",
    ),

    path(
        "documents/delete/<int:document_id>/",
        delete_document,
        name="delete_document",
    ),

    path(
        "chat/",
        chat,
        name="chat",
    ),

    path(
        "chat/<int:conversation_id>/",
        conversation,
        name="conversation",
    ),

]