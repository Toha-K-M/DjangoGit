# Generated by Django 3.0.5 on 2020-04-22 16:58

import datetime
from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GitEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('is_pull_request', models.BooleanField(default=False)),
                ('is_push', models.BooleanField(default=False)),
                ('action', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='GitRepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_repo', models.IntegerField()),
                ('name', models.CharField(max_length=250)),
                ('create_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gitrepo_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
