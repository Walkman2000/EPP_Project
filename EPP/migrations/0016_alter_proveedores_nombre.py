# Generated by Django 4.1.7 on 2023-03-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EPP', '0015_alter_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='nombre',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
