from django.db import models
import uuid

class Submission(models.Model):
    request_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4().hex)
    code = models.TextField()
    language = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.request_id:
            self.request_id = str(uuid.uuid4())
            # self.request_id = '2'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.language
    
class CodeResult(models.Model):
    request_id = models.CharField(max_length=100, unique=True)
    result = models.TextField()

    def __str__(self):
        return self.request_id