# Generated by Django 5.2.3 on 2025-06-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('empleado', 'Empleado'), ('cliente', 'Cliente')], default='cliente', max_length=20)),
            ],
        ),
    ]
