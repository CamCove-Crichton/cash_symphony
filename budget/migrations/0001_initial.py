# Generated by Django 5.0.1 on 2024-01-21 16:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('amount', models.CharField(max_length=12)),
                ('payment_type', models.IntegerField(choices=[(0, 'once_off'), (1, 'recurring')], default=0)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('budget_month', models.CharField(blank=True, max_length=7, null=True)),
                ('frequency', models.IntegerField(choices=[(0, 'NA'), (1, 'daily'), (2, 'weekly'), (3, 'monthly')], default=0)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['payment_date', 'created_on'],
            },
        ),
    ]