from django.contrib import admin
from coder_course.models import *
from coder_course.views import familias
# Register your models here.

admin.site.register(Insumos)

admin.site.register(Tareas)

admin.site.register(Rubros)

admin.site.register(Familias)

