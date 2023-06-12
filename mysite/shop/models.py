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
