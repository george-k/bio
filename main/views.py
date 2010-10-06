# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from main.decorators import render_to
from main.models import Contact
from main.forms import ContactForm


@render_to('show_contact.html')
def show_contact(request):
    """ Show contact """
    try:
        contact = Contact.objects.get(pk=1)
    except:
        contact = None
    return {'contact': contact}


@login_required
@render_to('edit_contact.html')
def edit_contact(request):
    """ Edit contact """
    #Get contact
    try:
        contact = Contact.objects.get(pk=1)
    except:
        return HttpResponseRedirect('/')
    #Handle request
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                data = form.cleaned_data
                contact.name = data['name']
                contact.surname = data['surname']
                contact.birthday = data['birthday']
                contact.bio = data['bio']
                contact.email = data['email']
                contact.phone = data['phone']
                contact.save()
            except:
                form.profilesave_error = _('Contact save error. Try again.')
    else:
        form = ContactForm({'name': contact.name,
                            'surname': contact.surname,
                            'birthday': contact.birthday,
                            'bio': contact.bio,
                            'email': contact.email,
                            'phone': contact.phone
                            })
    return {'contact_form': form}
