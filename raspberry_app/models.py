from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    nomPrenom = models.CharField(max_length=200, default=' ')
    nom = models.CharField(max_length=100, default=' ')
    prenom = models.CharField(max_length=100, default=' ')
    date_ajout = models.DateTimeField(null=True)
    num_mobile = models.CharField(max_length=100, default=' ')
    num_personelle = models.CharField(max_length=100, default=' ')
    num_prof = models.CharField(max_length=100, default=' ')
    image = models.CharField(max_length=100, default='image.png')
    email = models.EmailField(max_length=100, default=' ')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    class Meta:
        db_table = 'raspberry_app_contact'

    def __unicode__(self):
        return u"%d" % self.contact_id


class Message(models.Model):
    msg_id = models.AutoField(primary_key=True)
    date_envoie = models.DateTimeField()
    msg_body = models.CharField(max_length=160, default=' ')
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    destinataire = models.CharField(max_length=160, default=' ')
    contact = models.ManyToManyField(Contact)
    etat = models.IntegerField(default=0)

    class Meta:
        db_table = 'raspberry_app_message'

    def __unicode__(self):
        return u"%d" % self.msg_id


class Conversation(models.Model):
    conv_id = models.AutoField(primary_key=True)
    utilisateur = models.OneToOneField(User)
    contact = models.OneToOneField(Contact)
    class Meta:
        db_table = 'raspberry_app_conversation'

    def __unicode__(self):
        return u"%d" % self.msg_id
