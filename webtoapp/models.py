from django.db import models

class insertbutton(models.Model):
    buttonColor = models.CharField(max_length= 60)


class buttoninfo(models.Model):
    Button_letter = models.CharField(max_length=80)
    Button_height = models.IntegerField()
    Button_width = models.IntegerField()
    Button_Starting_xpoint = models.IntegerField()
    Button_Starting_ypoint = models.IntegerField()