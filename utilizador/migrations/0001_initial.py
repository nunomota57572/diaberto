# Generated by Django 3.0.3 on 2020-06-25 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuracoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='utilizador',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('Telefone', models.IntegerField(default='0')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('TipoUtilizador', models.CharField(choices=[('Participante', 'Participante'), ('Administrador', 'Administrador'), ('Colaborador', 'Colaborador'), ('Coordenador', 'Coordenador'), ('Professor Universitario', 'Professor Universitário')], default='Participante', max_length=30)),
                ('Estado', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('Curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracoes.cursos', verbose_name='Curso:')),
                ('Departamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracoes.departamentos', verbose_name='Departamento:')),
                ('UO', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configuracoes.uos', verbose_name='Unidade Organica:')),
            ],
            options={
                'verbose_name_plural': 'Utilizadores',
                'db_table': 'utilizador',
            },
        ),
        migrations.CreateModel(
            name='colab',
            fields=[
                ('id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('UO', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'colaborador',
            },
        ),
        migrations.CreateModel(
            name='coord',
            fields=[
                ('id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('UO', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'coordenador',
            },
        ),
    ]
