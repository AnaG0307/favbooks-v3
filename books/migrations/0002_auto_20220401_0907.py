# Generated by Django 3.2 on 2022-04-01 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_sub_category', models.CharField(max_length=254)),
                ('book_friendly_sub_category', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='book_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.sub_category'),
        ),
    ]
