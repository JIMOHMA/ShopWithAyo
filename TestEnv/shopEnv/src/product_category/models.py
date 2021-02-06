from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=200)
  price = models.FloatField()

  category_status = (
    ('coats', 'coats'),
    ('jeans', 'jeans'),
    ('shirts', 'shirts'),
    ('sweats', 'sweats'),
  )
  # this is either jeans, shirts, coats or sweats
  category = models.CharField(
    max_length=200,
    choices=category_status,
    blank=True,
    default='',
    help_text='Clothing Category',
    )

  image = models.ImageField(null=True, blank=True)

  def __str__(self):
    return self.name

	# @property
	# def imageURL(self):
	# 	try:
	# 		url = self.image.url
	# 	except:
	# 		url = ''
	# 	return url