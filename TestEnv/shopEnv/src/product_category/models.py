from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

  # this is either jeans, shirts, coats or sweats
  category_status = (
    ('coats', 'coats'),
    ('jeans', 'jeans'),
    ('shirts', 'shirts'),
    ('sweats', 'sweats'),
  )

  name = models.CharField(max_length=200)
  price = models.FloatField()
  image = models.ImageField(null=True, blank=True)
  category = models.CharField(
    max_length=200,
    choices=category_status,
    blank=True,
    default='',
    help_text='Clothing Category',
    )

  def __str__(self):
    return self.name

  #@property decorator allows us to access the url as a attribute instead of a method
  @property
  def imageURL(self):
    try:
      url = self.image.url
    except:
      url = ''
    return url

  def get_absolute_url(self):
    return f"details/{self.id}/"


class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=200, null=True)
  email = models.CharField(max_length=200, null=True)

  def __str__(self):
    return self.name

class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
  date_ordered = models.DateTimeField(auto_now_add=True)
  complete = models.NullBooleanField(default=False, null=True, blank=False)
  transaction_id = models.CharField(max_length=200, null=True)

  def __str__(self):
    return str(self.id)

class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
  quantity = models.IntegerField(default=0, null=True, blank=True)
  date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
  address = models.CharField(max_length=200, null=False)
  city = models.CharField(max_length=200, null=False)
  state = models.CharField(max_length=200, null=False)
  zipcode = models.CharField(max_length=200, null=False)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.address