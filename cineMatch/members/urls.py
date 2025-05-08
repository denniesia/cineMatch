from django.urls import path
from cineMatch.members.views import login_user, signup, logout_user
urlpatterns = [
    path('login/', login_user, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_user, name='logout'),
]