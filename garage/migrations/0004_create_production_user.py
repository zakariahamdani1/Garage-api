import os

from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_production_user(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Token = apps.get_model("authtoken", "Token")

    username = os.getenv("PRODUCTION_USERNAME")
    email = os.getenv("PRODUCTION_EMAIL")
    password = os.getenv("PRODUCTION_PASSWORD")

    if not username or not password:
        return

    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            "email": email or "",
            "password": make_password(password),
            "is_staff": True,
            "is_superuser": True,
        },
    )

    if not created:
        user.email = email or user.email
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

    token, _ = Token.objects.get_or_create(user=user)

    print(f"PRODUCTION TOKEN: {token.key}")


class Migration(migrations.Migration):

    dependencies = [
        ("garage", "0003_alter_repair_mechanic"),
        ("authtoken", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_production_user),
    ]