from django.db import models
from users.models import User

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversation {self.id} with {self.user.username}"

class MemoryEntry(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='memory_entries', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"MemoryEntry {self.id} in conversation {self.conversation.id}"
