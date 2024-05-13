# Generated by Django 4.2 on 2024-05-13 00:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paiment_choice',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('choice_amount', models.IntegerField(verbose_name='choice amount')),
                ('device_amount', models.IntegerField(default=0, verbose_name='device amount')),
                ('rest', models.IntegerField(default=0, verbose_name='rest')),
                ('card_uuid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paiment_choice', to='kiosk_core.card', verbose_name='card uuid')),
            ],
        ),
    ]