from django.contrib import admin
from django.contrib import admin
from .models import Product, ProductMarketDetails
from .models import (
    Market,
    Product,
    Activity,
    SalesData,
    ProductMarketDetails,
    # PlanningDashboardDetails,
    QRCodeCutomizationTemplates,
)


class SalesDataAdmin(admin.ModelAdmin):
    list_display = ("product", "market", "from_date", "to_date")
    search_fields = (
        "product__product_name",
        "product__product_description",
        "market__market_name",
        "from_date",
        "to_date",
    )


class ProductMarketDetailsInline(admin.TabularInline):  # or admin.StackedInline
    model = ProductMarketDetails
    extra = 0  # Number of extra forms to display
    verbose_name = "Extra Field"
    verbose_name_plural = "Extra Fields"
    # template = "custom_inline_formset.html"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductMarketDetailsInline]


admin.site.register(Activity)
# admin.site.register(Product)
admin.site.register(ProductMarketDetails)
admin.site.register(Market)
admin.site.register(SalesData, SalesDataAdmin)
# admin.site.register(PlanningDashboardDetails)
admin.site.register(QRCodeCutomizationTemplates)
