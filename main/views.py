# -*- coding: utf-8 -*-
from decorators import render_to
from main.models import Contact


@render_to('show_contact.html')
def show_contact(request):
    try:
        contact = Contact.objects.get(pk=1)
    except:
        contact = None
    return {'contact':contact}

