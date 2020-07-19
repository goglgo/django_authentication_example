# Generated by Django 3.0.8 on 2020-07-19 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.CharField(choices=[('BRONZE', 'Bronze'), ('SILVER', 'Silver'), ('PLATINUM', 'Platinum'), ('DIAMOND', 'Diamond')], default='BRONZE', max_length=10)),
                ('userForeignKey', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RoleUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
