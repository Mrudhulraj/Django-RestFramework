from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, employee, validated_data):
        newEmp = Employee(**validated_data)
        employee.name = newEmp.name
        newEmp.save()
        return newEmp


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)
