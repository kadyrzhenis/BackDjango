from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
