import django
from django.conf import settings

# Asegúrate de que Django esté configurado
if not settings.configured:
    settings.configure(DATABASES={'default': {'ENGINE': 'django.db.backends.postgresql', 'NAME': 'guarani25', 'USER': 'postgres', 'PASSWORD': 'postgres', 'HOST': 'localhost', 'PORT': '5432'}})
    django.setup()

from django.contrib.auth.hashers import make_password

password_en_texto_plano = 'handling'
hashed_password = make_password(password_en_texto_plano)
print(hashed_password)