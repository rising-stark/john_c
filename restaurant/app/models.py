from django.db import models

class Company(models.Model):
  id = models.AutoField(primary_key=True)
  company_name = models.CharField(max_length=100)
  company_benefits_detail = models.TextField(null=True, blank=True)
  company_bonus_detail = models.TextField(null=True, blank=True)
  company_equity_detail = models.TextField(null=True, blank=True)

class Recipient(models.Model):
  id = models.AutoField(primary_key=True)
  recipient_firstname = models.CharField(max_length=100)
  recipient_lastname = models.CharField(max_length=100)
  recipient_salary = models.IntegerField(default=0, null=True, blank=True)
  recipient_bonus = models.IntegerField(default=0, null=True, blank=True)
  recipient_equity = models.IntegerField(default=0, null=True, blank=True)
