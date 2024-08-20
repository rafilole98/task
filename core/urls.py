from django.urls import path
from . import views


app_name = "core"


urlpatterns=[
    path('',views.show_all_persons_view,name="show_all_persons"),
    path('jobs-list/',views.show_all_jobs_view,name="show_all_jobs"),
    path('jobdetail-list/',views.show_all_personjobdetails_view,name="show_all_jobdetails"),
    path('person/create/',views.create_person_view,name="create_person"),
    path('person-detail/<int:pk>/',views.showpersondetail_view,name="show_person_detail"),
    path('job/create/',views.create_job_view,name="create_job"),
    path('jobdetail/create/',views.create_personjob_view,name="create_jobdetail"),
    ]