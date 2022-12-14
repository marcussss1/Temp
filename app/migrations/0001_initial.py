# Generated by Django 4.1.2 on 2022-10-18 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag1', models.CharField(max_length=256)),
                ('tag2', models.CharField(max_length=256)),
                ('tag3', models.CharField(max_length=256)),
                ('tag4', models.CharField(max_length=256)),
                ('tag5', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('number', models.IntegerField()),
                ('answers', models.IntegerField()),
                ('counting_tags', models.IntegerField()),
                ('text_answers', models.TextField()),
                ('counting_answers', models.IntegerField()),
                ('tag_names', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tag')),
            ],
        ),
    ]
