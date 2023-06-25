from django.db import models

from decimal import Decimal
import random

class Trader(models.Model):
    # ...fields...

    def generate_profit_loss(self):
        return Decimal(random.uniform(-10, 10))
