from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length = 20,
        choices = (
        ('1', "Member"),
        ('2', "Admin"),
        ))

    def __str__(self):
        return f'{self.user}'
    
    
class Expense(models.Model):
    name = models.CharField(max_length=140, blank=True, null=True)
    date_of_expense = models.DateField()
    category = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amount = models.PositiveIntegerField(default=0)
    created_by = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.created_by} - {self.name}'

# Temp users 
# member1@xyz.com - 1234 (member)
# member2@xyz.com - 1234 (member)
# member3@xyz.com - 1234 (member)
# admin1@xyz.com - 1234 (admin)
# admin - admin (superuser)