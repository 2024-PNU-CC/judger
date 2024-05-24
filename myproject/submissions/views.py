from django.shortcuts import render, redirect
from .forms import SubmissionForm
from django.http import HttpResponseRedirect, JsonResponse
import pika
import myproject.settings as settings
import json
import uuid
from .models import CodeResult

def submit_code(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': '코드가 성공적으로 제출되었습니다!'})
    else:
        form = SubmissionForm()
    return render(request, 'submissions/submit_code.html', {'form': form})

def success(request):
    return render(request, 'submissions/success.html')

def redirect_to_submit(request):
    return HttpResponseRedirect('/submit/')

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
        # body=str(message)
        body=json.dumps(message)
    )
    connection.close()

def send_code(request):
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            # 데이터베이스에 먼저 저장
            submission = form.save(commit=False)
            request_id = str(uuid.uuid4())
            submission.request_id = request_id
            submission.save()

            code = form.cleaned_data['code']
            language = form.cleaned_data['language']

            send_to_rabbitmq(request_id=request_id, code=code, language=language)

            return JsonResponse({'success': True, 'message': '코드가 성공적으로 제출되었습니다!'})
    else:
        form = SubmissionForm()
    return render(request, 'submissions/submit_code.html', {'form': form})

def get_result_by_request_id(request, request_id):
    try:
        result = CodeResult.objects.get(request_id=request_id)
        data = {
            'request_id': result.request_id,
            'result': result.result,
        }
        return render(request, 'submissions/submit_code.html', data)
    except CodeResult.DoesNotExist:
        return JsonResponse({"error": "Result not found"}, status=404)