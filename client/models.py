from djongo import models
from decimal import Decimal
import random
from django.conf import settings
from datetime import datetime
from django.utils import timezone
import uuid

class Trade(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    figures = models.FloatField()
    current_time = models.DateTimeField(default=timezone.now, null=False)

class Client(models.Model):
    name = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    initial_balance = models.FloatField()
    current_balance = models.FloatField()
    previous_balance = models.ArrayField(
        model_container=Trade,
        default=list,
        blank=True
    )

    def generate_profit_loss(self):
        return Decimal(str(random.uniform(-10, 10)))
    
