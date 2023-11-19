from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    brith_date=models.DateField()
    bigraphy=models.TextField(max_length=1000)

    def __str__(self):
        return self.name
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book_author')
    publish_date=models.DateTimeField(auto_now=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.title
class Review(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='review_book')
    reviewer_name=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    rate = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    

    

    def __str__(self):
        return self.reviewer_name

