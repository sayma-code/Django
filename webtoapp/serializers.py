from rest_framework import serializers
import sys
sys.path.append(".")
from .models import buttoninfo

class ButtonSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ['Button_letter', 'Button_height', 'Button_width', 'Button_Starting_xpoint', 'Button_Starting_ypoint']
        model = buttoninfo