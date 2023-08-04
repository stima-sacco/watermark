from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from os import path
from django.conf import settings

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=255, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class ImageModel(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='blogpic')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        photo = Image.open(self.image.path)
        draw = ImageDraw.Draw(photo)
        width, height = photo.size
        myword = "MOMBASA CAR MARKET"
        margin = 10
        font_size=int(width/25)
        font_path = path.join(settings.BASE_DIR, 'custom_fonts/Alverata-Bold.ttf')
        font = ImageFont.truetype(font_path, font_size)
        # textwidth, textheight = draw.textsize(myword, font)
        x, y = int(width/2), int(height/2)# - (int(height) - int(height/10))
        draw.text((x,y), myword, (240, 240, 240, 240), font=font, stroke_width=3, stroke_fill='#eeeeee', anchor='ms')
        photo.save(self.image.path)