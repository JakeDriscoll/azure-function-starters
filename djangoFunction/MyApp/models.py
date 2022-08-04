from django.db import models


class TestTimeZones(models.Model):
    name = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)
    random_int = models.IntegerField()
# Create your models here.
