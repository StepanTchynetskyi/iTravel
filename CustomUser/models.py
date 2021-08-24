import datetime
import uuid

from django.db import models
from utils.pool import pool_manager
from django.utils import timezone


class CustomUser(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4,null=False, editable=False)
    user_name = models.CharField(max_length=55, null=False,blank=False)
    name = models.CharField(max_length=55, null=False,blank=False)
    last_name = models.CharField(max_length=55, null=False,blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)


    def save(self, *args, **kwargs):
        if not self.created:
            self.created = timezone.now()
        return super(CustomUser, self).save(*args, **kwargs)

    def to_dict(self):
        return {
            "user_name": self.user_name,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email
        }

    def __str__(self):
        return 'User' + str(self.user_name)

    def get_user_by_id(self):
        table = "\"CustomUser_customuser\""
        with pool_manager as conn:
            conn.cursor.execute(f'INSERT INTO {table} (user_id,user_name, name, last_name, email, password,created_at,updated_at) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(uuid.uuid4(),'name1','name2','name3','name@gmail.com','password',datetime.datetime.now(),datetime.datetime.now()))
            return None
