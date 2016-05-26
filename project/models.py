from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
	user = models.ForeignKey(User)
	project_name = models.CharField(max_length=100)
	creation_date = models.DateTimeField('date created')
	is_active = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)

	def __str__(self):
		return self.project_name

	def activate(self):
		self.is_active = True
		self.save()

	def deavtivate(self):
		self.is_active = False
		self.save()

	def delete(self):
		self.is_deleted = True
		self.save()

	def undelete(self):
		self.is_deleted = False
		self.save()

class ProjectTeamMember(models.Model):
	"""docstring for project team member"""
	project = models.ForeignKey(Project)
	user = models.ForeignKey(User)
	join_date = models.DateTimeField('date joined')
	is_suspended = models.BooleanField(default=False)
	is_removed = models.BooleanField(default=False)

	def suspend(self):
		self.is_suspended = True
		self.save()

	def keepon(self):
		self.is_suspended = False
		self.save()

	def doRemove(self):
		self.is_removed = True
		self.save()

	def undoRemove(self):
		self.is_removed = False
		self.save()

	def __str__(self):
		return self.user