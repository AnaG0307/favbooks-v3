from django.db import models


class Category(models.Model):
    """
    Meta class to correct the "categorys" incorrect spelling in the admin site
    """
    class Meta:
        verbose_name_plural = "Categories"

    book_category = models.CharField(max_length=254)
    book_friendly_category = models.CharField(
        max_length=254, null=True, blank=True
        )

    def __str__(self):
        return self.book_category

    def get_friendly_name(self):
        return self.book_friendly_category


class Sub_Category(models.Model):

    """
    Meta class to correct the "categorys" incorrect spelling in the admin site
    """
    class Meta:
        verbose_name_plural = "Sub_Categories"

    book_sub_category = models.CharField(max_length=254)
    book_friendly_sub_category = models.CharField(
        max_length=254, null=True, blank=True
        )

    def __str__(self):
        return self.book_sub_category

    def get_friendly_name(self):
        return self.book_friendly_sub_category


class Type(models.Model):
    book_type = models.CharField(max_length=254)
    book_friendly_type = models.CharField(
        max_length=254, null=True, blank=True
        )

    def __str__(self):
        return self.book_type

    def get_friendly_name(self):
        return self.book_friendly_type


class Book(models.Model):
    book_category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    book_sub_category = models.ForeignKey(
        'Sub_Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    book_type = models.ForeignKey(
        'Type', null=True, blank=True, on_delete=models.SET_NULL
        )
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    synopsis = models.TextField()
    price_hardcover = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    price_paperback = models.DecimalField(
        max_digits=6, decimal_places=2
        )
    price_electronic = models.DecimalField(
        max_digits=6, decimal_places=2
        )
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    cover_url = models.URLField(max_length=1024, null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)


class Comment(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    book_title = models.ForeignKey(
        'Book',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="comments")
    approved = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.content} by {self.name}'

    def number_of_comments(self):
        return self.approved.count()
