# Generated by Django 3.0.4 on 2020-03-31 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamMembers', '0004_auto_20200330_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='testBS',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
    ]