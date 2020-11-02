from django.urls import path
from . import views
from django.conf.urls import url

app_name = "Vote"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DeptDetailView.as_view(), name='deptdetail'),
    path('Department/(?P<user>[\w\-]+)/$', views.DeptView.as_view(), name='dept'),
    path('Faculty/(?P<user>[\w\-]+)/$', views.FacultyView.as_view(), name='faculty'),
    path('SUG/(?P<user>[\w\-]+)/$', views.SUGView.as_view(), name='sug'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
    path('accounts/login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('otp/verification/(?P<user>[\w\-]+)/$', views.getotp, name="getotp"),
    path('sendotp/confirm/(?P<user>[\w\-]+)/$', views.sendotp, name="sendotp"),
]