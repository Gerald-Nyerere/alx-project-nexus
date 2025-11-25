from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    # Self-referencing field for parent categories
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories')
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "categories"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name