from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_parrafos_options'),  # Asegurate que coincida con tu última migración existente
    ]

    operations = [
        migrations.AddField(
            model_name='parrafos',
            name='numero_de_parrafo',
            field=models.IntegerField(null=True),
        ),
    ]
