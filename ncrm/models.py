from django.conf import settings
from django.db import models
from django.utils import timezone

class B_Client(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name_second_name = models.TextField()
    loyalty_card = models.IntegerField()
    Description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    telephone_num = models.TextField()

    def b2b_client(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name_second_name

