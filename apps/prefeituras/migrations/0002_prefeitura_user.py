# 0002_prefeitura_user.py
from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('prefeituras', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='prefeitura',
            name='user',
            field=models.ForeignKey(on_delete=models.PROTECT, to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]
