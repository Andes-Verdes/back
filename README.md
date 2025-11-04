# Andes Verdes – Backend  
API REST para la gestión de información de Parques Nacionales

Andes Verdes es una aplicación destinada a mejorar la comunicación entre los Parques Nacionales Argentinos y el público general.  
Este repositorio contiene el **backend del proyecto**, desarrollado con **Django + Django REST Framework**, encargado de manejar los datos, usuarios, fauna, flora, imágenes y contenido informativo.

---

## Tecnologías utilizadas

- **Python 3**
- **Django 5**
- **Django REST Framework**
- **MySQL**
- **Entorno virtual con venv**

---

## Características principales del backend

API REST completa (CRUD) para:
- Parques Nacionales  
- Fauna  
- Flora  
- Imágenes  
- Párrafos descriptivos  
- Usuarios  

Soporte para **roles de usuario**:
- `admin`: puede crear, editar y eliminar contenido  
- `user`: solo lectura en la app  

Endpoints separados para:
- Registro (Sign Up)
- Inicio de sesion (LogIn)

Estructura basada en las prácticas del estándar IEEE 830.

---

## Estructura del proyecto
AndesVerdes-Back/
│── andesverdes/ # Configuraciones principales de Django
│── app/ # Aplicación donde está toda la API
│ ├── models.py # Modelos (Faunas, Parques, etc.)
│ ├── views.py # APIViews
│ ├── serializer.py # Serializadores de DRF
│ ├── urls.py # Rutas de la API
| ├── Otros archivo PY
│── env
│── requirements.txt
│── manage.py

## Instalación y configuración

### Clonar el repositorio
bash:
git clone https://github.com/tuusuario/AndesVerdes-Back.git
cd AndesVerdes-Back
### Crear y activar entorno virtual
python -m venv env
env\Scripts\activate    
### Instalar dependencias
pip install -r requirements.txt
### Configurar DB en settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'andesverdes',
        'USER': 'root',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
### Aplicar migraciones
python manage.py makemigrations
python manage.py migrate
### Ejecutar el servidor
python manage.py runserver

### Sistema de usuarios y roles
El modelo **Usuarios** incluye el campo:
rol = models.CharField(choices=[('admin','Administrador'),('user','Usuario')])
### Comportamiento del rol en la app
Los administradores pueden agregar fauna, flora, párrafos, parques, imágenes.
Los usuarios normales solo pueden consultar (GET).
El frontend usa este rol para mostrar u ocultar el botón Dashboard.
### Ejemplo de Sign Up
REQUEST:
POST /signup/
{
  "nombre": "Vicente",
  "apellido": "Sanchez",
  "correo": "vicente@example.com",
  "contraseña": "123456",
  "rol": "user"
}
RESPONSE:
{
  "message": "Usuario registrado exitosamente."
}
### Como saber si un usuario es Admin en el frontend
Ejemplo de respuesta del backend al obtener un usuario:
{
  "id_usuario": 3,
  "nombre": "Benicio",
  "correo": "benicio@example.com",
  "rol": "admin"
}
El frontend usa este campo asi:
if (data.rol === "admin") {
    mostrarDashboard();
}
### Futuras mejoras
Hash de contraseñas
Implementación de JWT
Mapas interactivos con geolocalización real
Prestadores turísticos
Sistema de alertas y estado de senderos
Chatbot inteligente
Recuperación de contraseña

### Equipo de trabajo (Primer prototipo)
Vicente Sanchez Calfual: Scrum Master/Developer (Diseño y desarrollo)
Joaquin Ignacio Narvay: Developer/Testing (Desarrollo y testing)
Ezequiel David Rey: Developer/Testing (Desarrollo y testing)
Benicio Ferrer: Developer/Gestion (BACKEND developer)
Alumnos de la escuela N°713 "Juan Abdala Chayep"