from django.db import models
import datetime

# Create your models here.
class modelClass(models.Model):
    auto_field = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    number = models.BigIntegerField(default=1)
    boolean_field = models.BooleanField(default=False)
    #null_boolean_field = models.NullBooleanField()
    # comma_separated_field = models.CharField(
    #     validators=[comma_separated_field],
    #     max_length=255
    # )
    date_field = models.DateField(default=datetime.datetime.today())
    date_time_field = models.DateTimeField(default=datetime.datetime.now())
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    email_field = models.EmailField(default="")
    float_field = models.FloatField(default=0)
    
    file_field = models.FileField(upload_to='ppp/', default="")

    time_field = models.TimeField()
    def __str__(self):
        return self.name 