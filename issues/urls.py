from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_issue, name='report'),  # Report issue page
    path('success/<int:issue_id>/', views.success, name='success'),  # Success page after submission
    path('my-reports/', views.my_reports, name='my_reports'),  # Dashboard / Track Issues page
]