from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)  # Otomatik artırma olarak tanımlanmış birincil anahtar alanı
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
  
    
class Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    

class IHA(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE , related_name='iha_brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name='iha_category')
    model = models.ForeignKey(Model, on_delete=models.CASCADE , related_name='iha_model')
    weight = models.FloatField()

    def __str__(self):
        return f"{self.brand.name} - {self.model.name}"


