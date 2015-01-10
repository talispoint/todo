from django.db import models
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError

# Create your models here.

class Todo(models.Model):
	title = models.CharField(max_length = 100)
	finished = models.BooleanField(default = False)

	def __str__(self):
		return self.title + " is " + ("not " if not self.finished else "") + "finished."

	def clean(self):
		if len(self.title) == 0:
			raise ValidationError("title cannot be empty.")

	# Force django to validate the model when calling save().
	def validate_model(sender, **kwargs):
	    if 'raw' in kwargs and not kwargs['raw']:
	        kwargs['instance'].full_clean()
	pre_save.connect(validate_model, dispatch_uid='validate_models')		