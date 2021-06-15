#  Django's guide on Model layer
#  https://docs.djangoproject.com/en/3.2/topics/db/models/#model-inheritance

from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ["age"]

    def __str__(self):
        return "%s %s" % (self.__class__.__name__, self.name)


class Worker(CommonInfo):
    job = models.CharField(max_length=50)


class Unmanaged(models.Model):
    guardian = models.CharField(max_length=100)

    class Meta:
        abstract = True
        ordering = ["guardian"]
        managed = False


class Student(CommonInfo):
    school_class = models.CharField(max_length=10)

    class Meta(CommonInfo.Meta):
        pass


# Abstract base classes with related models


class Post(models.Model):
    title = models.CharField(max_length=50)


class Attachment(models.Model):
    post = models.ForeignKey(
        Post,
        models.CASCADE,
        related_name="attached_%(class)s_set",
        related_query_name="attached_%(app_label)s_%(class)ss",
    )
    content = models.TextField()

    class Meta:
        abstract = True


class Comment(Attachment):
    is_spam = models.BooleanField(default=False)


class Link(Attachment):
    url = models.URLField()


# multi-table inheritance


class Chef(models.Model):
    name = models.CharField(max_length=50)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


class Rating(models.Model):
    rating = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["-rating"]


class Restaurant(Place, Rating):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    chef = models.ForeignKey(Chef, models.SET_NULL, null=True, blank=True)

    class Meta(Rating.Meta):
        db_table = "my_restaurant"


class ItalianRestaurant(Restaurant):
    serves_gnocchi = models.BooleanField(default=False)
