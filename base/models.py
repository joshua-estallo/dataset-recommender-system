import os
from django.db import models
from django.utils.translation import gettext as _
from django.core.validators import FileExtensionValidator

class Dataset(models.Model):
  title = models.CharField(_("Title"), max_length=255,)
  overview = models.TextField(_("Overview"), blank=True)
  description = models.TextField(max_length=255, blank=True)
  data_type = models.CharField(max_length=255, blank=True)
  category = models.CharField(max_length=255, blank=True)
  tags = models.CharField(max_length=255, blank=True)
  file_format = models.CharField(max_length=255, blank=True)
  research_title = models.CharField(max_length=255, blank=True)
  project_head = models.CharField(max_length=255, blank=True)
  members = models.CharField(max_length=255, blank=True)
  date_uploaded = models.DateField(auto_now_add=True, blank=True, null=True)
  source = models.CharField(max_length=255, blank=True)
  link = models.CharField(max_length=255, blank=True)
  form = models.CharField(max_length=255, blank=True)
  file = models.FileField(
    upload_to="uploads/", 
    blank=True, 
    validators=[FileExtensionValidator(allowed_extensions=["zip", "rar"])]
  )
  archived = models.CharField(max_length=255, blank=True, default=0)
  def __str__(self):
    return self.title