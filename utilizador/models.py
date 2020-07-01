from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from configuracoes.models import uos, departamentos, cursos

# Create your models here.

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,            
		)
		user.Estado = 1
		user.TipoUtilizador = 'Administrador'
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class utilizador(AbstractBaseUser):
    
    class ENUM(models.TextChoices):
        PARTICIPANTE = 'Participante', ('Participante')
        ADMINISTRADOR = 'Administrador', ('Administrador')
        COLABORADOR = 'Colaborador', ('Colaborador')
        COORDENADOR = 'Coordenador', ('Coordenador')
        PROFESSOR = 'Professor Universitario', ('Professor Universitário')

    id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=200)
    email = models.EmailField(verbose_name="email",max_length=60, unique=True)
    Telefone = models.IntegerField(default="0")
    #password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    UO = models.ForeignKey(uos, verbose_name="Unidade Organica:", on_delete=models.CASCADE, blank=True, null=True)
    Departamento = models.ForeignKey(departamentos, verbose_name="Departamento:", on_delete=models.CASCADE, blank=True, null=True)
    Curso = models.ForeignKey(cursos, verbose_name="Curso:", on_delete=models.CASCADE, blank=True, null=True)
    TipoUtilizador = models.CharField(max_length=30,choices=ENUM.choices,default=ENUM.PARTICIPANTE,)
    Estado = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = MyAccountManager()

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Utilizadores"
        db_table = "utilizador"

    def __str__(self):
        return self.username 

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

class colab(models.Model):
    id = models.OneToOneField(utilizador, on_delete=models.CASCADE, default=None,primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    UO = models.CharField(max_length=200)
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "colaborador"
    def __str__(self):
        return self.username

class coord(models.Model):
    id = models.OneToOneField(utilizador, on_delete=models.CASCADE, default=None,primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    UO = models.CharField(max_length=200)
    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "coordenador"
    
    def __str__(self):
        return self.username