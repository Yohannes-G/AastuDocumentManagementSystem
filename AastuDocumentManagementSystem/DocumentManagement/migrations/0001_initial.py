# Generated by Django 3.0.7 on 2021-08-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=50)),
                ('cours_name', models.CharField(max_length=50)),
                ('cours_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('doc_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('doc_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('folder_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('folder_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('history_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('media_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('media_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message_name', models.CharField(max_length=50)),
                ('message_content', models.TextField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('notify_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('notify_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('user_sex', models.CharField(max_length=10)),
            ],
        ),
    ]