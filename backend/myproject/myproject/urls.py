from django.contrib import admin
from django.urls import path, include
from submissions.views import redirect_to_submit, get_result_by_request_id, render_submission_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/', include('submissions.urls')),
    path('', redirect_to_submit, name='home'),
    path('result/<str:request_id>', get_result_by_request_id, name='get_result_by_request_id'),
    path('submit/<str:request_id>', render_submission_page, name='render_submission_page')
]
