# Generated by Django 5.0.7 on 2024-08-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogly', '0006_post_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]