# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-06-26 21:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raspberry_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.CharField(default='image.png', max_length=100),
        ),
        migrations.AddField(
            model_name='message',
            name='contact',
            field=models.ManyToManyField(to='raspberry_app.Contact'),
        ),
        migrations.AddField(
            model_name='message',
            name='destinataire',
            field=models.CharField(default=' ', max_length=160),
        ),
        migrations.AddField(
            model_name='message',
            name='etat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='utilisateur',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_ajout',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nom',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='nomPrenom',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='contact',
            name='num_mobile',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='num_personelle',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='num_prof',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='prenom',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='utilisateur',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='msg_body',
            field=models.CharField(default=' ', max_length=160),
        ),
        migrations.AlterField(
            model_name='message',
            name='msg_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Utilisateur',
        ),
    ]