from __future__ import unicode_literals

import datetime

from django.http import HttpResponse
from django.shortcuts import render

from vacancy.getvacancy import update_vacancy


def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    update_vacancy()
    return HttpResponse(html)
