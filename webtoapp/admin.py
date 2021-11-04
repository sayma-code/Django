from django.contrib import admin
from . import models
from .models import insertbutton
from .models import buttoninfo

admin.site.register(insertbutton)
admin.site.register(buttoninfo)