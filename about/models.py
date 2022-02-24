from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Testimonial(models.Model):
    choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="testimonials")
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], default=1, choices=choices)
    content = models.TextField(max_length=1000)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.name} rated {self.rating}'