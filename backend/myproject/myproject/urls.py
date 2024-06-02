from django.contrib import admin
from django.urls import path
from submissions.views import my_view, get_result_by_request_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/my-endpoint/', my_view, name='my-endpoint'),
    path('api/result/<str:request_id>', get_result_by_request_id, name='get_result_by_request_id'),
]
