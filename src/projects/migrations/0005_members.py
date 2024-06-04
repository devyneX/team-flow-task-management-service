# Generated by Django 5.0.6 on 2024-05-31 10:04

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_created_by_project_owner_project_updated_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberSerializer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('deleted', models.BooleanField(default=False, verbose_name='deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('created_by', models.UUIDField()),
                ('updated_by', models.UUIDField()),
                ('user', models.UUIDField()),
                (
                    'project',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='members',
                        related_query_name='member',
                        to='projects.project'
                    )
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
