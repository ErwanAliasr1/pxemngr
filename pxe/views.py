from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from common import *
from models import *

def localboot(request, mac):
    system = get_object_or_404(System, macaddress__mac=simplify_mac(mac))
    set_next_boot(system, settings.PXE_LOCAL)
    return HttpResponse("Next boot set to local", mimetype="text/plain")
