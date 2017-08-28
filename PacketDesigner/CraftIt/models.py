from django.db import models

class PacketDetails(models.Model):
    db_srcIP = models.CharField(max_length=64,blank=True)
    db_destIP = models.CharField(max_length=250,blank=True)
    db_summary = models.CharField(max_length=500,blank=True)
    db_srcPort = models.IntegerField(null=True)
    db_destPort = models.IntegerField(null=True)
    db_payload = models.CharField(max_length=32,blank=True)
    db_flags = models.CharField(max_length=6,blank=True)
    db_ttlValue = models.IntegerField(null=True)
    db_protocol= models.CharField(max_length=8,blank=True)


    def __str__(self):
        return self.db_destIP


# Create your models here.
