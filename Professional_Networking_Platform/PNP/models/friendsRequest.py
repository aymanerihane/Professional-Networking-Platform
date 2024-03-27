from django.db import models

class FriendRequest(models.Model):
    sender = models.ForeignKey('PNP.User', on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey('PNP.User', on_delete=models.CASCADE, related_name='received_requests')