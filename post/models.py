
from django.core.validators import MinLengthValidator
from django.db import models
# from FurryFunnies.author.models import Author
# from FurryFunnies.author.validators import validate_letters, validate_digits


# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        validators=[MinLengthValidator(5)],
        error_messages={
            'unique': "Oops! That title is already taken. How about something fresh and fun?",
        }
    )

    image_url = models.URLField(
        help_text="Share your funniest furry photo URL!",
        blank=False,
    )

    content = models.TextField(
        blank=False
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    author = models.ForeignKey(
        to='author.Author',
        on_delete=models.CASCADE,
        related_name="post",
    )
