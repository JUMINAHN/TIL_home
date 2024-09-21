# Generated by Django 4.2.16 on 2024-09-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('api_url', models.URLField()),
                ('documentation_url', models.URLField()),
                ('auth_required', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('additional_info', models.TextField()),
            ],
        ),
    ]
