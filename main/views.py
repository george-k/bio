# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.simplejson import dumps
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as __

from main.decorators import render_to
from main.forms import ContactForm
from main.models import Contact


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
                form.errors['save_error'] = __('Contact save error. Try again.')
        else:
            form.errors['errors_message'] = __("Correct errors, please.")
        if request.is_ajax():
            if form.errors:
                response = {'result': 'error'}
                response['errors'] = form.errors
                return HttpResponse(dumps(response))
            else:
                return HttpResponse(dumps({'result': 'ok'}))
    else:
        form = ContactForm(instance=contact)
    return {'contact_form': form}
