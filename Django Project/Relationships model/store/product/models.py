from django.db import models


# ==========================================
# Category Model
# One Category -> Many Products
# Example:
# Men
#   ├── Puma Shoe
#   ├── Nike Shoe
#   └── Adidas Shoe
# ==========================================
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


# ==========================================
# Product Model
# Har Product ek Category se belong karega
# Example:
# Product = Puma Shoe
# Brand = Puma
# Category = Men
# ==========================================
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100)

    # One Category -> Many Products
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return f"{self.product_name} ({self.brand_name})"


# ==========================================
# Product Variant / Details
#
# Ek Product ke multiple sizes ho sakte hain
#
# Puma Shoe
#   ├── Size M -> ₹1222
#   ├── Size L -> ₹2222
#   └── Size XL -> ₹2500
#
# Isliye ForeignKey use hua hai
# (One Product -> Many Variants)
# ==========================================
class Details(models.Model):

    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='details')

    size = models.CharField(max_length=5,choices=SIZE_CHOICES)

    price = models.PositiveIntegerField()

    discount = models.PositiveIntegerField(default=0)

    off = models.PositiveIntegerField(default=0)

    description = models.TextField(blank=True,null=True)

    class Meta:

        # Same product ke liye same size
        # sirf ek baar allow hoga

        constraints = [
            models.UniqueConstraint(
                fields=['product', 'size'],
                name='unique_product_size'
            )
        ]

    def __str__(self):
        return f"{self.product.product_name} - {self.size}"