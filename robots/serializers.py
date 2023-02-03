from rest_framework import serializers
from .models import Robot


class RobotSerializer(serializers.ModelSerializer):

    class Meta:
        model = Robot
        fields = '__all__'

    def validate_model(self, value):
        if not Robot.objects.filter(model=value):
            raise serializers.ValidationError("Такой модели не существует!")
        return value

    def create(self, validated_data):
        return Robot.objects.create(**validated_data)
