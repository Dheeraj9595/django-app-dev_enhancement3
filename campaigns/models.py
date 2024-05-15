from django.db import models
from .constants import CATEGORY_CHOICES
from django.contrib.auth.models import User
from brands.models import Brand, Division, LocalBrand, Category
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=500)
    key_contact_first_name = models.CharField(max_length=500)
    key_contact_last_name = models.CharField(max_length=500)
    key_contact_email_address = models.EmailField()
    secondary_contact_first_name = models.CharField(
        max_length=500, blank=True, null=True
    )
    secondary_contact_last_name = models.CharField(
        max_length=500, blank=True, null=True
    )
    secondary_contact_email_address = models.EmailField(blank=True, null=True)
    date_added = models.DateField(auto_now=True)
    date_updated = models.DateField(auto_now_add=True)
    updated_by = models.CharField(max_length=500, null=True)
    history = HistoricalRecords()

    def __str__(self) -> str:
        return f"{self.pk} - {self.campaign_name}"


class CampaignAdditionalDetails(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    # category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_landing_page_on_an_external_third_party_site = models.BooleanField(default=False)
    does_landing_page_include_1pd_capture_or_signup = models.BooleanField(default=False)
    does_landing_page_include_option_to_purchase = models.BooleanField(default=False)
    if_yes_is_there_an_incentive_to_purchase = models.BooleanField(default=False)
    planned_launch_date = models.DateField()

    class Meta:
        verbose_name = "campaign additional details"
        verbose_name_plural = "campaign additional details"

    def __str__(self) -> str:
        return f"{self.pk} - {self.campaign.campaign_name} campaign additional details"


class CategoryUserLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    class Meta:
        verbose_name = _('Category User Permissions')
        verbose_name_plural = _('Category Access Permissions')

    # def __str__(self):
    #     return f"{self.user.username} - {self.category}"
    def __repr__(self):
        return f"CategoryUserLink(user={self.user.username}, category={self.category})"
