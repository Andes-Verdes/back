from django.contrib import admin
from app.models import Faunas
from app.models import FaunasHasParques
from app.models import Floras
from app.models import Imagenes
from app.models import Parques
from app.models import ParquesFloras
from app.models import Parrafos
from app.models import Usuarios

admin.site.register(Faunas)
admin.site.register(FaunasHasParques)
admin.site.register(Floras)
admin.site.register(Imagenes)
admin.site.register(Parques)
admin.site.register(ParquesFloras)
admin.site.register(Parrafos)
admin.site.register(Usuarios)
