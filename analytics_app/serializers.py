from rest_framework import serializers
from .models import ShopView, ProductView, AnalyticsProduct, Shop, Product

# --- Shop Serializer ---
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['external_id', 'name']

# --- ShopView Serializer ---
class ShopViewSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()  # Nested serializer
    viewed_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ShopView
        fields = ['id', 'shop', 'viewed_at']

    def create(self, validated_data):
        # Shop məlumatını çıxarırıq
        shop_data = validated_data.pop('shop')

        # Shop-u yoxlayırıq: varsa götür, yoxdursa yarat
        shop, created = Shop.objects.get_or_create(
            external_id=shop_data['external_id'],
            defaults={'name': shop_data['name']}
        )

        # ShopView-u yaradırıq
        shop_view = ShopView.objects.create(
            shop=shop,
            **validated_data
        )
        return shop_view


class ProductViewSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    viewed_at = serializers.DateTimeField(read_only=True)  # avtomatik hazırkı vaxt

    class Meta:
        model = ProductView
        fields = ['id', 'product', 'viewed_at']



class AnalyticsProductSerializer(serializers.ModelSerializer):
    shop = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all())
    product_variation = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = AnalyticsProduct
        # Bütün sahələr göstərilsin
        fields = ['id', 'shop', 'product_variation', 'count', 'original_price', 'sale_price', 'created_at']