# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Faunas(models.Model):
    id_fauna = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'faunas'


class FaunasHasParques(models.Model):
    id_fauna = models.OneToOneField(Faunas, models.DO_NOTHING, db_column='id_fauna', primary_key=True)  # The composite primary key (id_fauna, id_parque) found, that is not supported. The first column is selected.
    id_parque = models.ForeignKey('Parques', models.DO_NOTHING, db_column='id_parque')

    class Meta:
        managed = False
        db_table = 'faunas_has_parques'
        unique_together = (('id_fauna', 'id_parque'),)


class Floras(models.Model):
    id_flora = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'floras'


class Imagenes(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    leyenda = models.CharField(max_length=45)
    url = models.CharField(max_length=255)
    id_parque = models.ForeignKey('Parques', models.DO_NOTHING, db_column='id_parque')
    id_fauna = models.ForeignKey(Faunas, models.DO_NOTHING, db_column='id_fauna')
    id_flora = models.ForeignKey(Floras, models.DO_NOTHING, db_column='id_flora')
    is_carrusel = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'imagenes'


class Parques(models.Model):
    id_parque = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'parques'


class ParquesFloras(models.Model):
    id_parque = models.OneToOneField(Parques, models.DO_NOTHING, db_column='id_parque', primary_key=True)  # The composite primary key (id_parque, id_flora) found, that is not supported. The first column is selected.
    id_flora = models.ForeignKey(Floras, models.DO_NOTHING, db_column='id_flora')

    class Meta:
        managed = False
        db_table = 'parques_floras'
        unique_together = (('id_parque', 'id_flora'),)


class Parrafos(models.Model):
    id_parrafo = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    id_parque = models.ForeignKey(Parques, models.DO_NOTHING, db_column='id_parque')
    id_fauna = models.ForeignKey(Faunas, models.DO_NOTHING, db_column='id_fauna')
    id_flora = models.ForeignKey(Floras, models.DO_NOTHING, db_column='id_flora')

    class Meta:
        managed = False
        db_table = 'parrafos'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    contraseña = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'usuarios'
