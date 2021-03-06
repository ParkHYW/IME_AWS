# Generated by Django 4.0.1 on 2022-05-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0006_human'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200)),
                ('meaning', models.TextField()),
                ('href', models.URLField(max_length=1000, null=True)),
                ('firstkeyword', models.CharField(max_length=200, null=True)),
                ('secondkeyword', models.CharField(max_length=200, null=True)),
                ('lastkeyword', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='human',
            name='href',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
