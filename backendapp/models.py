from django.db import models
from django.db.models import CASCADE

class Currency(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.code

class Rate(models.Model):
    source = models.ForeignKey(Currency, related_name='base', on_delete=CASCADE)
    target = models.ForeignKey(Currency, on_delete=CASCADE)
    rate = models.DecimalField(max_digits=17, decimal_places=8)

    def __unicode__(self):
        return '%s / %s = %s' % (self.source, self.target, self.rate)