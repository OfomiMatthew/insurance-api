# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit-claim/', views.submit_claim, name='submit-claim'),
    # path('download/<int:pk>/', views.download_file, name='download-file'),
]
