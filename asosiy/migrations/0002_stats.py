# Generated by Django 4.1.5 on 2023-03-30 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('miqdor', models.PositiveIntegerField()),
                ('olchov', models.CharField(max_length=30)),
                ('summa', models.PositiveIntegerField()),
                ('tolandi', models.PositiveIntegerField()),
                ('qoldi', models.PositiveIntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.client')),
                ('mahsulot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.mahsulot')),
            ],
        ),
    ]
