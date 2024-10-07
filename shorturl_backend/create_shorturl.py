import os
import django

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shorturl_backend.settings")  # Ajusta esto según el nombre de tu configuración
django.setup()

from urls.models import ShortURL, User  # Asegúrate de que el nombre de tu aplicación sea correcto

# Crear un ShortURL
url = ShortURL.objects.create(original_url="https://example.com")

# Crear un usuario
user = User.objects.create_user(username="testuser", password="password123")

# Añadir la URL a los favoritos del usuario
user.favoritos.add(url)  # Asegúrate de que esta relación esté definida en tu modelo
user.save()

print("ShortURL y usuario creados correctamente.")