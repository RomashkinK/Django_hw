# Generated by Django 5.0.6 on 2024-05-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('image', models.URLField(max_length=300)),
                ('price', models.PositiveIntegerField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
    ]
