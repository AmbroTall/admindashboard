from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Customer(models.Model):
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    phone = models.IntegerField()
    slug = models.SlugField(max_length=50,null=True, blank=True)

    class Meta:
        ordering: ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('indoor','indoor'),
        ('outdoor','outdoor'),
    )
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY,null=True)
    price = models.FloatField()
    tags = models.ManyToManyField(Tags)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Order(models.Model):
    STATUS = (
        ('delivered', 'delivered'),
        ('pending', 'pending'),
    )
    admin_user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, max_length=10)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.customer.name} has {self.product.name} on {self.date}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.customer}+{self.product}')
        super().save(*args, **kwargs)
