# Generated by Django 3.0.7 on 2021-09-10 13:03

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_time', models.DateTimeField(auto_now_add=True)),
                ('message_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message_cc', models.BooleanField(default=False)),
                ('message_description', models.TextField(max_length=256)),
                ('message_file', models.FileField(blank=True, upload_to='')),
                ('message_unread', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('office_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('office_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='office', to='DocumentManagement.Office')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ReplyMessage',
            fields=[
                ('reply_time', models.DateTimeField(auto_now_add=True)),
                ('reply_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('reply_cc', models.BooleanField(default=False)),
                ('reply_description', models.TextField(max_length=256)),
                ('reply_file', models.FileField(blank=True, upload_to='')),
                ('reply_unread', models.BooleanField(default=True)),
                ('reply_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_receiver', to=settings.AUTH_USER_MODEL)),
                ('reply_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_sender', to=settings.AUTH_USER_MODEL)),
                ('replyed_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replyed_message', to='DocumentManagement.Message')),
            ],
        ),
        migrations.AddField(
            model_name='office',
            name='office_type_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='office_type', to='DocumentManagement.Type'),
        ),
        migrations.AddField(
            model_name='message',
            name='message_receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='message_sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
