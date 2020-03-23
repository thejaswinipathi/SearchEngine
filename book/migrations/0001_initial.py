# Generated by Django 2.2.5 on 2020-03-23 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=128)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=128)),
                ('count', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
            ],
        ),
    ]