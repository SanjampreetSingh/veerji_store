from django.db import migrations
from django.db.models.functions.datetime import TruncTime
import environ

from api.user.models import User
from api.locality.models import Locality

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


class Migration(migrations.Migration):

    def seed_data(apps, schema_editor):
        loc = Locality(name="G Block SBS Nagar")
        loc.save()

        user = User(
            name=env('SU_NAME'),
            email=env('SU_EMAIL'),
            is_staff=True,
            is_superuser=True,
            phone=env('SU_PHONE'),
            locality=loc
        )
        user.set_password(env('SU_PASSWORD'))
        user.save()

    dependencies = []
    operations = [
        migrations.RunPython(seed_data),
    ]
