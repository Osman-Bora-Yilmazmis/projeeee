# Generated by Django 4.1.8 on 2023-05-18 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_alter_hijyenmodel_idari_calisan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hijyenmodel',
            name='form_gonderen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hijyen_formlar', to=settings.AUTH_USER_MODEL),
        ),
    ]
