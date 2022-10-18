from django.contrib import admin
from divorcements.models import Divorcement
from divorcements.models import DivorcementChild

admin.site.register(Divorcement)
admin.site.register(DivorcementChild)