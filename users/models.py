from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy
from phonenumber_field.modelfields import PhoneNumberField
from django.template.defaultfilters import slugify


class Profile(models.Model):
    """
    The user profile form
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name="Аватар")
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name="URL")
    address = models.CharField(max_length=250, verbose_name='Адрес', blank=False)
    phone = PhoneNumberField(null=False, blank=False, verbose_name='Номер телефона')
    city = models.CharField(max_length=100, verbose_name='Город', blank=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('users:profile', kwargs={'slug': self.slug})
