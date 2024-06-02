from django.contrib import admin
from django.urls import path
from submissions.views import my_view, get_result_by_request_id

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('submit/', include('submissions.urls')),
    # path('', redirect_to_submit, name='home'),
    # path('result/<str:request_id>', get_result_by_request_id, name='get_result_by_request_id'),
    # path('submit/<str:request_id>', render_submission_page, name='render_submission_page'),
    path('api/my-endpoint/', my_view, name='my-endpoint'),
    path('api/result/<str:request_id>', get_result_by_request_id, name='get_result_by_request_id')
]
