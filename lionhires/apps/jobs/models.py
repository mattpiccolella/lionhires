from django.db import models

class LinkedInUser(models.Model):
  linked_in_id = models.CharField(max_length = 80)
  first_name = models.CharField(max_length = 80)
  last_name = models.CharField(max_length = 80)
  def __unicode__(self):
    return self.first_name + " " + self.last_name
  @classmethod
  def create(cls, id, first, last):
    user = cls(linked_in_id=id, first_name=first, last_name=last)
    return user
