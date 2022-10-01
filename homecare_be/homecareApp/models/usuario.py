from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UsuarioManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Los usuarios deben tener el nombre de usuario')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password):
      user = self.create_user(
      username=username,
      password=password,
      )
      user.is_admin = True
      user.save(using=self._db)
      return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    id_Usuario = models.BigAutoField(primary_key=True)
    username=models.CharField('username', max_length=15, unique=True)
    password = models.CharField('Contrasena', max_length = 256)
    id_perfil= models.CharField('Perfil', max_length=35)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UsuarioManager()
    USERNAME_FIELD = 'username'

