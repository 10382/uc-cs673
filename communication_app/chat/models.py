from django.db import models

# Create your models here.


class rooms(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    creation_date = models.DateField()
    delete_date = models.DateField(null=True)
    
class messages(models.Model):
   room_id = models.IntegerField(null=False)
   sender_user_name = models.CharField(max_length=255)
   receiver_user_id = models.CharField(max_length=255)
   content = models.CharField(max_length=255)
   sent_date = models.DateTimeField()
   received_date = models.DateTimeField()
   read_date = models.DateTimeField(null=True)


class testing(models.Model):
   room_id = models.IntegerField(null=False)
   sender_user_id = models.CharField(max_length=255)
    