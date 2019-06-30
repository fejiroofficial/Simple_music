from django.urls import path
from .views import (ListCreateSongsView, SongsOperationsView,
                    LoginView, RegisterUsersView)


urlpatterns = [
    path('songs/', ListCreateSongsView.as_view(), name="songs-list-create"),
    path('songs/<int:pk>/', SongsOperationsView.as_view(),
         name="songs-operations"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register")
]
