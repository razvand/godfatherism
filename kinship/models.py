from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=100)
	birthday = models.DateTimeField(null=True)
	birth_location = models.CharField(max_length=50, blank=True)
	affiliation = models.CharField(max_length=32, blank=True)
	biography_link = models.URLField(max_length=200, blank=True)
	is_public = models.BooleanField(default=True)
	affiliation_update = models.DateTimeField(null=True)

	def __str__(self):
	        return self.name


class Kinship(models.Model):
	ego = models.ForeignKey(Person, related_name='ego')
	kinship_type = models.CharField(max_length=32)
	godfather = models.ForeignKey(Person, related_name='godfather')
	godmother = models.ForeignKey(Person, related_name='godmother')
	date = models.DateTimeField()
	
	def __str__(self):
	        return self.ego + " has been " + self.kinship_type + " by " + self.godfather + " and " + self.godmother + " on " + self.date 


class Relationship(models.Model):
	ego = models.ForeignKey(Person, related_name='ego_')
	ego_position = models.CharField(max_length=50)
	appointee = models.ForeignKey(Person, related_name='appointee')
	action_type = models.CharField(max_length=20)
	appointee_position = models.CharField(max_length=50)
	date = models.DateTimeField()
	start_exercise = models.DateTimeField(null=True)
	end_exercise = models.DateTimeField(null=True)

	def __str__(self):
	        return self.ego + " in position of " + self.ego_position + " does action " + self.action_type + " for " + self.appointee_position + " to " + self.appointee
