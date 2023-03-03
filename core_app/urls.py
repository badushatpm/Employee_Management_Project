from django.urls import path
from core_app.views import EmployeeView, EmployeeDetailView

urlpatterns = [
    path('', EmployeeView.as_view()),
    path('<str:pk>', EmployeeDetailView.as_view())
]