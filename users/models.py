from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse_lazy
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify


class User(AbstractUser):
    """
    The user model
    """
    first_name = models.CharField(verbose_name="Имя", max_length=150, blank=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150, blank=True)
    email = models.EmailField(verbose_name="Email адрес", unique=True)
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name="Аватар")
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name="URL")
    address = models.CharField(max_length=250, verbose_name='Адрес')
    phone = PhoneNumberField(null=False, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, verbose_name='Город')

    REQUIRED_FIELDS = ("first_name", "last_name", "email", "photo", "address", "phone", "city")

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('users:profile', kwargs={'slug': self.slug})
