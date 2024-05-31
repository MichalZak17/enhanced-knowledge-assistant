from django.db import models
from users.models import User

class Email(models.Model):
    sender = models.ForeignKey(User, related_name='sent_emails', on_delete=models.CASCADE)
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.recipient} from {self.sender.username}"

class EmailTemplate(models.Model):
    name = models.CharField(max_length=100)
    subject_template = models.CharField(max_length=255)
    body_template = models.TextField()

    def __str__(self):
        return self.name
