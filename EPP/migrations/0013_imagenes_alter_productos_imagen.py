# Generated by Django 4.1.7 on 2023-03-13 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EPP', '0012_alter_clientes_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes')),
            ],
            options={
                'db_table': 'Imagenes',
            },
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EPP.imagenes'),
        ),
    ]