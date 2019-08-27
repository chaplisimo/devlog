from django.db import models

# Create your models here.
class Entry(models.Model)
	title = CharField(max_length=60)
	content = TextField()
	pub_date = DateTimeField(auto_now_add = True)
	# author = 
	

	