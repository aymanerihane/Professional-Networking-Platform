
import json
from django.db import models

class Message(models.Model):
    messages = models.TextField(default="[]")
    media = models.TextField(default="[]")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    participent = models.ManyToManyField('PNP.User')

    def send_message(self, new_message):
        current_messages = self.get_messages_list()
        current_messages.append(new_message)
        self.messages = json.dumps(current_messages)
        self.save()

    def delete_message(self, index):
        current_messages = self.get_messages_list()
        if 0 <= index < len(current_messages):
            del current_messages[index]
            self.messages = json.dumps(current_messages)
            self.save()

    def receive_message(self):
        return self.get_messages_list()

    def get_messages_list(self):
        try:
            return json.loads(self.messages)
        except (json.JSONDecodeError, ValueError):
            return []

    def get_media_list(self):
        try:
            return json.loads(self.media)
        except (json.JSONDecodeError, ValueError):
            return []
