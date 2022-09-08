from platform import release
from django.db import models
import uuid
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    released_at = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    rating = models.DecimalField(default=0.0, decimal_places=1,max_digits=2, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-rating']