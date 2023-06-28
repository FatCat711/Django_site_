from django.contrib.auth.models import User
from django.db import models


def category_image_directory_path(instance: "Category", filename: str) -> str:
    return "categories/category_{pk}/image/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


def subcategory_image_directory_path(instance: "SubCategory", filename: str) -> str:
    return "subcategories/subcategory_{pk}/image/{filename}".format(
        pk=instance.pk,
        filename=filename,
    )


class Category(models.Model):
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=category_image_directory_path, null=True, blank=True)
    subcategories = models.ManyToManyField("SubCategory", related_name="category")

    def __str__(self):
        return f"Category {self.title} #{self.pk}"


class SubCategory(models.Model):
    class Meta:
        verbose_name = "подкатегория"
        verbose_name_plural = "подкатегории"

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=subcategory_image_directory_path, null=True, blank=True)

    def __str__(self):
        return f"Subcategory {self.title} #{self.pk}"


class Product(models.Model):
    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    description = models.TextField(default="")
    fullDescription = models.TextField(default="")
    free_delivery = models.BooleanField(default=False)
    count = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    specifications = models.ManyToManyField("Specification", related_name="products")
    tags = models.ManyToManyField("Tag", related_name="products")
    # reviews = models.ManyToManyField("Review", related_name="products")
    rating = models.FloatField(default=0)
    limited = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)

    def get_rating(self):
        reviews = Review.objects.filter(product=self)
        if reviews:
            sum_rating = sum(review.rate for review in reviews)
            count_rating = Review.objects.all().count()
            self.rating = round(sum_rating / count_rating, 1)
            return self.rating
        return None

    def get_reviews_count(self):
        reviews = Review.objects.filter(product=self)
        return len(reviews)

    def get_images(self, obj):
        return {
            "src": obj.image.url,
            "alt": ""
        }

    def __str__(self):
        return f"Product {self.title} {self.price}(#{self.pk})"


def product_image_directory_path(instance: "ProductImage", filename: str) -> str:
    return "products/product_{pk}.images/{filename}".format(
        pk=instance.product.pk,
        filename=filename,
    )


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=product_image_directory_path)



class Specification(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"Specification {self.name} {self.value}"


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Tag #{self.pk} {self.name}"


class Review(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    text = models.TextField(default="")
    rate = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, related_name="reviews")

    def __str__(self):
        return f"Review #{self.pk} by {self.author}"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    delivery_type = models.CharField(max_length=30, default="")
    payment_type = models.CharField(max_length=30, default="")
    total_cost = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.CharField(max_length=30, default="")
    city = models.CharField(max_length=30, default="")
    address = models.CharField(max_length=100, default="")
    products = models.ManyToManyField(Product, related_name="products")
    user = models.ForeignKey(User, related_name="user", on_delete=models.PROTECT)

    def __str__(self):
        return f"Order #{self.pk}"
