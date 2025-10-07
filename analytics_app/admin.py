from django.contrib import admin
from .models import AnalyticsProduct, ShopView, ProductView,Product,Shop

# Satışları admin paneldə göstərmək
admin.site.register(AnalyticsProduct)

# Mağaza baxışları
admin.site.register(ShopView)

# Məhsul baxışları
admin.site.register(ProductView)

admin.site.register(Product)
admin.site.register(Shop)


