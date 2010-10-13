# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.simplejson import dumps
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext

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
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            try:
                form.save()
                form.result = True
                form.message = ugettext(u'Contact updated successfully')
            except:
                form.result = False
                form.message = ugettext(u'Contact save error. Try again.')
        else:
            form.result = False
            form.message = ugettext(u"Correct errors, please")
        if request.is_ajax():
            response = {'message': form.message}
            if not form.result:
                response['result'] = 'error'
                response['errors'] = form.errors
            else:
                response['result'] = 'ok'
            return HttpResponse(dumps(response))
    else:
        form = ContactForm(instance=contact)
        form.message = ''
    return {'contact_form': form}
