from django.urls import path
from .views import submit_code, success, send_code, get_result_by_request_id

urlpatterns = [
    path('', submit_code, name='submit_code'),
    path('success/', success, name='success'),
    path('send_code/', send_code, name='send_code'),
    path('result/<str:request_id>/', get_result_by_request_id, name='get_result_by_request_id'),
]