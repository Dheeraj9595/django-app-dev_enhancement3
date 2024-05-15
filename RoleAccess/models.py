from brands.models import LocalBrand, Category, Brand
from products.models import Market
from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import Group


class Role(Group):
    class Meta:
        proxy = True
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self):
        return self.name


Group._meta.verbose_name = 'Role'
Group._meta.verbose_name_plural = 'Roles'


class CustomUserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class AccessTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, blank=True)
    markets = models.ManyToManyField(Market, blank=True)
    brands = models.ManyToManyField(Brand, blank=True)

    class Meta:
        verbose_name = _('User Permissions')
        verbose_name_plural = _('Access Restrictions')

    def __repr__(self):
        return f"AccessTable(user={self.user.username}, category={self.category}, brand={self.brands}, market={self.markets})"

    def __str__(self):
        return f"{self.user}"