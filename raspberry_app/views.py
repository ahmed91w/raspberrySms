from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core import serializers
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from datetime import datetime
from twilio.rest import TwilioRestClient
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
import os
from raspberry_app.models import *
from django.shortcuts import get_object_or_404



def composeur(request):
    return render(request, 'pages/composeur.html')


def index(request):
    contact = Contact.objects.all().filter(utilisateur=request.user).count()
    messages = Message.objects.all().filter(utilisateur=request.user).count()
    return render(request, 'pages/index.html', {'contacts': contact, 'messages': messages})


def shutdown(request):
    os.system("sudo shutdown -h now")


def sendSMS(request):
    if request.method == 'POST':
        bodymsg = request.POST.get('msg')
        to_number = request.POST.get('contact')
        # to_number = "+212600100367"
        account_sid = "account_sid"
        auth_token = "auth_token"
        client = TwilioRestClient(account_sid, auth_token)
        message = client.messages.create(
            body=bodymsg,
            to='+' + to_number,
            from_="+14249032602")

        saveMessage = Message(date_envoie=datetime.now(), msg_body=bodymsg, utilisateur=request.user,
                              destinataire=to_number, etat=1)
        saveMessage.save()

        response = {'status': -1, 'id': saveMessage.msg_id, 'message': bodymsg, 'to': to_number,
                    'date_envoie': saveMessage.date_envoie, 'etat': saveMessage.etat}
        return JsonResponse(response)
    else:
        status = 404
        return HttpResponse(status)


def loginView(request):
    return render(request, 'login.html')


def login_check(request):
    if request.method == 'POST':
        u_username = request.POST.get('username')
        u_password = request.POST.get('password')
        user = authenticate(username=u_username, password=u_password)
        if user is not None:
            if user.is_active:
                login(request, user)
                response = {'status': 1, 'message': 'Ok'}
                return JsonResponse(response)
            else:
                response = {'status': -1, 'message': 'Le mot de passe est valide, mais le compte a ete desactive'}
                return JsonResponse(response)
        else:
            response = {'status': -2, 'message': 'Le nom d\'utilisateur ou mot de passe sont incorrects.'}
            return JsonResponse(response)
    else:
        response = {'status': -3, 'message': 'est pas une requete POST.'}
        return JsonResponse(response)


def costum_logout(request):
    logout(request)
    return redirect(loginView)


def profil(request):
    utilisateur_courant = request.user
    return render(request, 'pages/profil.html', {'user': utilisateur_courant})


def my_scheduled_job():
    print("this is a cronjob")


def conversation(request, contact_num):
    print(contact_num)
    contact = Contact.objects.get(num_mobile__contains=contact_num)
    messages = Message.objects.filter(destinataire__contains=contact_num)
    messages = messages.filter(utilisateur=request.user)

    return render(request, 'pages/conversation.html',
                  {'contact': contact, 'messages': messages})


def goToConversation(request, contact_num):
    print(contact_num)
    contact = Contact.objects.filter(num_mobile__contains=contact_num)
    messages = Message.objects.filter(destinataire__contains=contact_num)
    messages = messages.filter(utilisateur=request.user)
    if (contact):
        return render(request, 'pages/conversation.html',
                      {'contact': contact, 'messages': messages})
    else:
        contact.num_mobile = contact_num
        return render(request, 'pages/conversation.html',
                      {'contact': contact, 'messages': messages})


def newContact(request):
    if request.method == 'POST':

        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        contact = Contact(nomPrenom=nom + " " + prenom, nom=nom, prenom=prenom, image="image.png",
                          date_ajout=datetime.now(), email=email, num_mobile=mobile, utilisateur=request.user,
                          num_prof=" ", num_personelle=" ")
        contact.save()
        return redirect(contacts)
    else:
        return redirect(addContact)


def editContact(request, id):
    contact = Contact.objects.get(pk=id)
    return render(request, "pages/edit_contact.html", {'contact': contact, 'id': id})


def updateContact(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        contact = Contact.objects.get(pk=id)
        print(contact)
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        contact.nom = nom
        contact.prenom = prenom
        contact.nomPrenom = nom + " " + prenom
        contact.email = email
        contact.num_mobile = mobile
        contact.save()
        return redirect(contacts)
    else:
        return redirect(addContact)


def addContact(request):
    return render(request, "pages/add_contact.html")


def removeMsg(request, id):
    print(id)
    msg = Message.objects.get(pk=id)
    msg.delete()
    print("message id=" + id + "was deleted")
    response = {'status': 1, 'message': 'Message Supprimer avec succes.'}
    return JsonResponse(response)


def addMsg(request, id_contact):
    contact = Contact.objects.get(pk=id_contact)
    messages = Message.objects.all().filter(utilisateur=request.user)
    messages = messages.filter(destinataire__contains=contact.num_mobile)
    return render(request, "pages/conversation.html", {'messages': messages, 'contact': contact})


def register_view(request):
    return render(request, "sign-in.html")


def edit_profil_view(request):
    return render(request, "pages/edit_profil.html")


def profil_update(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        u_fname = request.POST.get('fname')
        u_lname = request.POST.get('lname')
        u_email = request.POST.get('email')
        user.email = u_email
        user.first_name = u_fname
        user.last_name = u_lname
        user.save()
        return redirect(profil)
    else:
        return redirect(edit_profil_view)


def edit_password(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        u_pass = request.POST.get('password')
        user.set_password(u_pass)
        user.save()
        return redirect(profil)
    else:
        return redirect(edit_profil_view)


def contacts(request):
    user_contacts = Contact.objects.all().filter(utilisateur=request.user)
    return render(request, "pages/contacts.html", {'contacts': user_contacts})


def removeContact(request, id):
    user_contact = Contact.objects.get(pk=id)
    user_contact.delete()
    return redirect(contacts)


def messages(request):
    messages = Message.objects.all().filter(utilisateur=request.user)

    return render(request, "pages/messages.html", {'messages': messages})


def deleteAllMessages(request):
    messages = Message.objects.all().filter(utilisateur=request.user)
    for m in messages:
        m.delete()
        print(m.msg_id)
    response = {'status': 1, 'message': 'Messages Supprimes avec succes.'}
    return JsonResponse(response)
