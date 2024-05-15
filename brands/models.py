from django.db import models
from django.contrib.auth.models import Group


class LocalBrand(models.Model):
    id = models.AutoField(primary_key=True, db_column="local_brand_id")
    local_brand_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.local_brand_name


class Division(models.Model):
    id = models.AutoField(primary_key=True, db_column="division_id")
    division = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.division


class Category(models.Model):
    id = models.AutoField(primary_key=True, db_column="category_id")
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    brand_code = models.CharField(
        max_length=100, primary_key=True, db_column="brand_code"
    )
    division = models.OneToOneField(
        Division, on_delete=models.CASCADE, null=True, blank=True
    )
    local_brand = models.OneToOneField(LocalBrand, on_delete=models.CASCADE)
    global_brand_name = models.CharField(max_length=200, null=True, blank=True)
    upc_ean_gtin = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.brand_code


from django.db import models
from django.contrib.auth.models import User
from .models import LocalBrand


class BrandUserLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    local_brands = models.ManyToManyField(LocalBrand)

    class Meta:
        verbose_name = "Brands Access Permissions"
        verbose_name_plural = "Brands Access Permissions"

    # def __str__(self):
    #     return f"{self.user.username} - {self.local_brand.local_brand_name}"
    def __str__(self):
        return f"{self.user.username} - {', '.join(str(brand) for brand in self.local_brands.all())}"
