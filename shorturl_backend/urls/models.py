from djongo import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):  # Usamos AbstractUser para integrar con la autenticación de Django
    favoritos = models.ArrayReferenceField(
        to='ShortURL',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='favorited_by_users'
    )  # Lista de URLs favoritas del usuario
    created_at = models.DateTimeField(default=timezone.now)
     # Añadir related_name para evitar conflicto
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='urls_user_groups', 
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='urls_user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
    def str(self):
        return self.username
    
class ShortURL(models.Model):
    _id = models.ObjectIdField()  # Campo para el ID único generado por MongoDB
    original_url = models.URLField()  # Campo para la URL original
    short_url = models.CharField(max_length=255)  # La URL corta generada
    created_at = models.DateTimeField(default=timezone.now)  # Fecha y hora de creación
    clicks = models.IntegerField(default=0)  # Contador de clics
    custom_alias = models.CharField(max_length=100, blank=True, null=True)  # Alias personalizado opcional
    favorited_by = models.ManyToManyField(User, related_name='favorited_urls', blank=True) # Lista de usuarios que marcaron esta URL como favorita

    class Meta:
        verbose_name = "Short URL"
        verbose_name_plural = "Short URLs"

    def str(self):
        return self.short_url       