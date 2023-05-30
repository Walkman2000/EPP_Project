from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.timezone import now

class CustomUserManager(BaseUserManager):
    def create_user(self, usuario, telefono, contraseña, password):
        if not usuario and not password:
            raise ValueError('Escribe el usuario y la contraseña')
        if password != contraseña:
            raise ValueError('Las contraseñas no coinciden')
        user = self.model(
            usuario = usuario,
            telefono = telefono,
            contraseña = contraseña,
            password = password
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    usuario = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=10)
    contraseña = models.CharField(max_length=50, null=False, blank=False, default="")
    password = models.BooleanField(max_length=50, null=False, blank=False, default="")
    last_login = models.DateTimeField(default=now)
    objects = CustomUserManager()

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['telefono', 'contraseña', 'password']

    def __str__(self):
        return f'{self.usuario}'

    class Meta:
        db_table = 'Usuarios'