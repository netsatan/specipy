from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class FoodOffering(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()

    def __str__(self):
        return "{}, {}".format(self.name, self.price)


class Person(models.Model):
    """Represents anyone for whom a Reading can be created - does refer to a user however is not a user itself.
    This is anyone who can report attendance as user is someone who can supervise such action - employer, parent etc."""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    food_offering = models.ForeignKey(FoodOffering, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return "id = {}, {} {}, {}, {}".format(self.pk, self.first_name, self.last_name, self.food_offering, self.user)


class Card(models.Model):
    tag_id = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.person}, {self.tag_id}"


class Reading(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    tag = models.ForeignKey(Card, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return "{}, {}, {}".format(self.person.first_name, self.tag.tag_id, self.created_datetime)


class Absence(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    day = models.DateField()
    is_planned = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.person.first_name} {self.person.last_name}, {self.day.__str__()}, planned: ${self.is_planned}"


class Holiday(models.Model):
    day = models.DateField()

    def __str__(self):
        return f"{self.day.__str__()}"


class PrepaidHours(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    prepaid_amount = models.IntegerField()


class DiscountDefinition(models.Model):
    description = models.CharField(max_length=100)
    is_percentage = models.BooleanField(default=False)
    value = models.IntegerField()


class Invoice(models.Model):
    person = models.ForeignKey(Person, on_delete=models.DO_NOTHING, null=False)
    discount = models.ForeignKey(DiscountDefinition, on_delete=models.DO_NOTHING, null=True)
    total = models.FloatField()
    start_range = models.DateField(verbose_name='start_range')
    end_range = models.DateField(verbose_name='end_range')


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    rate = models.FloatField()


class UnknownReading(models.Model):
    tag = models.CharField(max_length=150)
    created_datetime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return "{}, {}".format(self.tag, self.created_datetime)
