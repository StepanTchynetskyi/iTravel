from django.db import models


class CustomUser(models.Model):
    user_name = models.CharField('First Name', max_length=55, null=False,blank=False)
    name = models.CharField('First Name', max_length=55, null=False,blank=False)
    last_name = models.CharField('Last Name', max_length=55, null=False,blank=False)
    email = models.EmailField('Email', max_length=100, null=False, blank=False)
    password = models.CharField('Password', max_length=128, null=False, blank=False)

    def to_dict(self):
        return {
            "user_name": self.user_name,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email
        }

    def __str__(self):
        return 'User' + str(self.user_name)

