from django.db import models
from django.utils import timezone

RESULTS_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('X', 0),
)

class Bet(models.Model):
    author = models.CharField(max_length=30)
    value = models.IntegerField()
    result = models.CharField(max_length=1, choices=RESULTS_CHOICES, default='', null=False)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish_bet(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.value
