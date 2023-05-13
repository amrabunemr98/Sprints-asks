from django.urls import path
from.import views

urlpatterns = [
    # path ('welcome/', views.welcome, name='welcome'),
    path('Resume/', views.Resume, name='Resume'),
    path('list/', views.student_view, name='list'),
    path('courses/', views.courses_view, name='courses'),
]