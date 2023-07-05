
from django.urls import path
from users.views import LoginUserApiView, CreateUserApiView


urlpatterns = [
    path('login/', LoginUserApiView.as_view()),
    path('create/', CreateUserApiView.as_view()),
]
