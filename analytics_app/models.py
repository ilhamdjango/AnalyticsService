from django.db import models
from django.utils import timezone

# 1️⃣ Shops
class Shop(models.Model):
    external_id = models.BigIntegerField(unique=True)  # Xarici sistem üçün unik ID
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.external_id})"


# 2️⃣ Products
class Product(models.Model):
    external_id = models.BigIntegerField(unique=True)  # Xarici sistem üçün unik ID
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.external_id})"


# 3️⃣ ShopViews
class ShopView(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="views")
    viewed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Shop View - {self.shop}"


# 4️⃣ ProductViews
class ProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="views")
    viewed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Product View - {self.product}"


# 5️⃣ AnalyticsProducts
class AnalyticsProduct(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product_variation = models.ForeignKey(Product, on_delete=models.CASCADE)  # Product variation varsa ayrıca modellə əvəz oluna bilər
    count = models.IntegerField(default=0)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Analytics: {self.shop} / {self.product_variation}"
