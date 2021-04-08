from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=10000)

    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
            return Contact.objects.get(email = email)
        except:
            return False