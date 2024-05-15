from django.urls import path

from .views import (
    QRRequestFormView,
    SalesDataFormView,
    QRTemplateApplyView,
    QRCodeCustomizeView,
    PlanningDashboardFormView,
    ProductView,
    product_and_qr_list,
    redirect_to_product_change, QRRequestview, user_brands
)


urlpatterns = [
    path("qr_request_form/", QRRequestFormView.as_view(), name="qr_request_form"),
    path('qr_request_form/<int:product_id>/', QRRequestview.as_view(), name='edit_qr_request_form'),
    path("sales_data_form/", SalesDataFormView.as_view(), name="sales_data_form"),
    path(
        "qr_code_customize_form/",
        QRCodeCustomizeView.as_view(),
        name="qr_code_customize_form",
    ),
    path(
        "planning_dashboard_details_form/",
        PlanningDashboardFormView.as_view(),
        name="planning_dashboard_details_form",
    ),
    path(
        "qr_template_apply_form/",
        QRTemplateApplyView.as_view(),
        name="qr_template_apply_form",
    ),
    path("products/", ProductView.as_view(), name="productview"),
    path('products_list/', product_and_qr_list, name='product_list'),
    path('userbrands/', user_brands, name='user-brand-link'),
    path('products/redirect_to_product_change/<int:product_id>/', redirect_to_product_change, name='redirect_to_product_change'),
]
