from django.http import JsonResponse
import pika
import myproject.settings as settings
import json
from .models import CodeResult, Submission
from django.views.decorators.csrf import csrf_exempt

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
