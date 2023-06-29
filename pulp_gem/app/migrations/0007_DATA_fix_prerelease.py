# Generated by Django 4.2.2 on 2023-06-29 15:20

from django.db import migrations


def fix_prerelease(apps, schema_editor):
    GemContent = apps.get_model("gem", "GemContent")
    # This is a postgres posix regex
    # https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP
    GemContent.objects.exclude(version__regex=r"^\d+(?:re\.\d+)*$").update(prerelease=True)


class Migration(migrations.Migration):
    dependencies = [
        ("gem", "0006_gemremote_excludes_gemremote_includes_and_more"),
    ]

    operations = [
        migrations.RunPython(code=fix_prerelease, reverse_code=migrations.RunPython.noop, elidable=True),
    ]
