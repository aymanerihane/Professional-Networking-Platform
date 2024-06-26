
import json
from django.db import models

class Message(models.Model):
    message = models.TextField(default="[]")
    media = models.ManyToManyField('PNP.MessageMedia', related_name='message', blank=True)
    #
    room = models.ForeignKey('PNP.Room', on_delete=models.CASCADE)
    user = models.ForeignKey('PNP.User', on_delete=models.CASCADE)
    #
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

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

