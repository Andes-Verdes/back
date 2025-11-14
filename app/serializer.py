from rest_framework import serializers
from .models import Faunas
from .models import FaunasHasParques
from .models import Floras
from .models import Imagenes
from .models import Parques
from .models import ParquesFloras
from .models import Parrafos
from .models import Usuarios

class FaunasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faunas
        fields = '__all__'

class FaunasHasParquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaunasHasParques
        fields = '__all__'

class FlorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floras
        fields = '__all__'

class ImagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagenes
        fields = '__all__'

class ParquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parques
        fields = '__all__'

class ParquesFlorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParquesFloras
        fields = '__all__'

class ParrafosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parrafos
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id_user', 'name', 'surname', 'email', 'rol'] #No conviene devolver la contraseña profe