# Generated by Django 4.0.4 on 2023-05-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0004_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='audio/')),
            ],
        ),
    ]