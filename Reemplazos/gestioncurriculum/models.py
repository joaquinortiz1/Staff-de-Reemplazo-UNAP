from django.db import models


class Usuario(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class Curriculum(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    experience = models.TextField()
    skills = models.TextField()
    education = models.TextField()

    def __str__(self):
        return self.title


class SolicitudDeReemplazo(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='solicitudes_de_reemplazo')

    def __str__(self):
        return self.title


class PuntuacionDeCandidato(models.Model):
    candidate = models.ForeignKey(Curriculum, on_delete=models.CASCADE)
    solicitud_de_reemplazo = models.ForeignKey(SolicitudDeReemplazo, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.candidate.title} - {self.solicitud_de_reemplazo.title}"



