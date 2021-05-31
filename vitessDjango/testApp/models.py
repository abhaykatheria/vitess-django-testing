from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
    
class Event(models.Model):
    title = models.CharField(max_length=150)
    start_date = models.DateField()
    start_date_time = models.DateTimeField()
    duration = models.DurationField()
    organiser_email = models.EmailField()
    banner = models.ImageField()
    slug = models.SlugField()
    no_of_attendees = models.IntegerField()
    no_of_views = models.BigIntegerField()
    website = models.URLField()
    start_time = models.TimeField()
    summary = models.TextField()
    brochure = models.FileField()
    rating = models.FloatField()
    is_accepting_registration = models.BooleanField()

class Server(models.Model):
    uuid = models.UUIDField()
    ip = models.GenericIPAddressField()
    memory_in_mb = models.PositiveBigIntegerField()
    no_of_cores = models.PositiveSmallIntegerField()
    freq_in_ghz = models.SmallIntegerField()
    no_of_threads = models.PositiveIntegerField()
    binary_sig = models.BinaryField()
    cache_size = models.DecimalField()
    







