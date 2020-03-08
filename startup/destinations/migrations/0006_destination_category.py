# Generated by Django 2.2.5 on 2020-03-05 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('destinations', '0005_auto_20200305_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='category',
            field=models.CharField(choices=[('SP', 'Shopping'), ('NP', 'Nature & Parks'), ('MS', 'Museums'), ('LA', 'Landmarks'), ('MN', 'Monuments'), ('AG', 'Art Galleries'), ('WA', 'Water & Amusement Parks')], default='SP', max_length=100),
            preserve_default=False,
        ),
    ]