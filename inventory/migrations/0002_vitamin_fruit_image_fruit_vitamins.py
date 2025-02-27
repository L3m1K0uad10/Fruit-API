# Generated by Django 4.2 on 2024-11-29 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vitamin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='fruit',
            name='image',
            field=models.ImageField(default='/media/fruit_images/mango.jpg', upload_to='fruit_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fruit',
            name='vitamins',
            field=models.ManyToManyField(blank=True, related_name='fruits', to='inventory.vitamin'),
        ),
    ]
