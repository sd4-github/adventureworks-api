from django.db import models
import uuid

class Person(models.Model):
    businessentityid = models.BigIntegerField(primary_key=True)
    persontype = models.CharField(max_length=2)
    namestyle = models.BooleanField()
    title = models.CharField(max_length=8, blank=True, null=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50)
    suffix = models.CharField(max_length=10, blank=True, null=True)
    emailpromotion = models.IntegerField()
    additionalcontactinfo = models.TextField(blank=True, null=True)
    demographics = models.TextField(blank=True, null=True)
    rowguid = models.UUIDField(default=uuid.uuid4)
    modifieddate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = '"person"."person"'
