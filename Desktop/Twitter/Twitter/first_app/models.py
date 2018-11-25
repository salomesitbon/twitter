from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=264, unique=True)
	name     = models.CharField(max_length=264, unique=False)
	email    = models.EmailField()
	bio      = models.CharField(max_length=264, unique=False)

	def __repr__(self):
		return "<User {}>".format(self.name)

	def __str__(self):
		return self.name

class Tweet(models.Model):
	text     = models.CharField(max_length=140, unique=False)
	date     = models.DateField()
	user     = models.ForeignKey(User, on_delete=models.CASCADE)

	def __repr__(self):
		return"<Tweet {}>".format(self.text)

	def __str__(self):
		return self.text

	
