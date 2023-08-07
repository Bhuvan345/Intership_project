from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views, hod_views, staff_views, student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # login path
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='Logout'),

    # Profile Update
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # HOD pannel url
    path('Hod/home', hod_views.HOME, name='Hod_home'),
    path('Hod/student/add', hod_views.ADD_STUDENT, name='add_student'),
    path('Hod/student/view', hod_views.VIEW_STUDENT, name='view_student'),
    path('Hod/student/edit/<str:id>', hod_views.EDIT_STUDENT, name='edit_student'),
    path('Hod/student/update', hod_views.UPDATE_STUDENT, name='update_student'),
    path('Hod/student/delete/<str:admin>',
         hod_views.DELETE_STUDENT, name='delete_student'),

    path('Hod/staff/add', hod_views.ADD_STAFF, name='add_staff'),
    path('Hod/staff/view', hod_views.VIEW_STAFF, name='view_staff'),
    path('Hod/staff/edit/<str:id>', hod_views.EDIT_STAFF, name='edit_staff'),
    path('Hod/staff/update', hod_views.UPDATE_STAFF, name='update_staff'),
    path('Hod/staff/delete/<str:admin>',
         hod_views.DELETE_STAFF, name='delete_staff'),


    path('Hod/course/add', hod_views.ADD_COURSE, name='add_course'),
    path('Hod/course/view', hod_views.VIEW_COURSE, name='view_course'),
    path('Hod/course/edit/<str:id>', hod_views.EDIT_COURSE, name='edit_course'),
    path('Hod/course/update', hod_views.UPDATE_COURSE, name='update_course'),
    path('Hod/course/delete/<str:id>',
         hod_views.DELETE_COURSE, name='delete_course'),

    # Staff urls
    #     path('Staff/home', staff_views.HOME, name='staff_home')


]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
