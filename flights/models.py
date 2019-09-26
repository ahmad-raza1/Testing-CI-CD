from django.db import models

# Create your models here.

class Airport(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=25)

	def __str__(self):
		return f"{self.city} ({self.code})"


class Flight(models.Model):
	origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
	destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
	duration = models.IntegerField()

	def is_valid_flight(self):
		return (self.origin != self.destination) and (self.duration >= 0)

	"""
	# Add a method that raises "Validation errors" if the data is illogical.
	def clean(self):
		if self.origin == self.destination:
		    raise ValidationError("Origin and destination must be different.")
		elif self.duration < 1:
		    raise ValidationError("Duration must be positive.")

	# Call this method before trying to add data, overriding the default behavior of built-in `save`.
	def save(self, *args, **kwargs):
		self.clean()

		# This syntax now calls Django's own "save" function, adding this data to the DB (if `clean` was ok).
		super().save(*args, **kwargs)

	"""
	
	def __str__(self):
		return f"{self.id} - {self.origin} to {self.destination}"


class Passenger(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
