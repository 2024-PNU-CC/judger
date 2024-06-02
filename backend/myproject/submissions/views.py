from django.shortcuts import render
from .forms import SubmissionForm
from django.http import HttpResponseRedirect, JsonResponse
import pika
import myproject.settings as settings
import json
from .models import CodeResult, Submission
from django.views.decorators.csrf import csrf_exempt

# def submit_code(request):
#     if request.method == 'POST':
#         form = SubmissionForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True, 'message': '코드가 성공적으로 제출되었습니다!'})
#     else:
#         form = SubmissionForm()
#     return render(request, 'submissions/submit_code.html', {'form': form})

# def success(request):
#     return render(request, 'submissions/success.html')

# def redirect_to_submit(request):
#     return HttpResponseRedirect('/submit/')

def send_to_rabbitmq(request_id, code, language):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=settings.RABBITMQ_HOST,
            port=5672,
            credentials=pika.PlainCredentials('rabbitmq username ss', 'rabbitmq password ss')
        )
    )
    channel = connection.channel()

    channel.queue_declare(queue=settings.RABBITMQ_QUEUE_NAME)

    message = {
        'request_id': request_id,
        'code': code,
        'language': language,
    }
    channel.basic_publish(
        exchange='',
        routing_key=settings.RABBITMQ_QUEUE_NAME,
        body=json.dumps(message)
    )
    connection.close()

# def send_code(request):
#     if request.method == 'POST':
#         form = SubmissionForm(request.POST)
#         if form.is_valid():
#             submission = form.save(commit=False)
#             # request_id = str(uuid.uuid4())
#             # # request_id = '2'
#             # submission.request_id = request_id
#             submission.save()

#             request_id = form.cleaned_data['id']
#             code = form.cleaned_data['code']
#             language = form.cleaned_data['language']

#             send_to_rabbitmq(request_id=request_id, code=code, language=language)

#             return JsonResponse({'success': True, 'message': '코드가 성공적으로 제출되었습니다!', 'request_id': request_id})
#     else:
#         form = SubmissionForm()
#     return render(request, 'submissions/submit_code.html', {'form': form})

def get_result_by_request_id(request, request_id):
    try:
        result = CodeResult.objects.get(request_id=request_id)
        data = {
            'request_id': result.request_id,
            'result': result.result,
        }
        return JsonResponse(data=data)
    except CodeResult.DoesNotExist:
        return JsonResponse({"error": "Result not found"}, status=404)

# def render_submission_page(request, request_id):
#     form = SubmissionForm()
#     return render(request, 'submissions/submit_code.html', {'form': form, 'request_id': request_id})

@csrf_exempt
def my_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        code = data.get('code', '')
        id = data.get('id', '')
        language = data.get('language', '')
        
        snippet = Submission.objects.create(request_id=id, language=language, code=code)
        send_to_rabbitmq(request_id=id, code=code, language=language)

        return JsonResponse({'message': f'You sent: {code}'}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)