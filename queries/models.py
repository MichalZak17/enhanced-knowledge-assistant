from django.db import models
from users.models import User

class Query(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query by {self.user.username} at {self.created_at}"

class Response(models.Model):
    query = models.ForeignKey(Query, related_name='responses', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response at {self.created_at} for {self.query.id}"
