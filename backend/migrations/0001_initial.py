# Generated by Django 3.2.7 on 2021-09-20 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GitHubUser',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('oauth_token', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RepositoryTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('repository_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
