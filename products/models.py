from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image/', blank=True, null=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name










