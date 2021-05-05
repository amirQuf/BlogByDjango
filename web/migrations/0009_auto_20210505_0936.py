# Generated by Django 3.1 on 2021-05-05 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20210501_0909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='savepost',
            options={'ordering': ('-time',)},
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Post', to='web.post'),
        ),
    ]
