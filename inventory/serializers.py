from rest_framework import serializers

from .models import Fruit, Vitamin



class VitaminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitamin 
        fields = [
            'id',
            'name',
        ]

class FruitSerializer(serializers.ModelSerializer):
    vitamins = serializers.PrimaryKeyRelatedField(queryset = Vitamin.objects.all(), many = True, write_only = True)
    vitamin_details = VitaminSerializer(many = True, read_only = True, source = "vitamins")

    # Read only 
    # vitamins = VitaminSerializer(many = True, read_only = True)
    class Meta:
        model = Fruit
        fields = [
            'id',
            'name',
            'price',
            'vitamins',
            'vitamin_details',
            'image',
        ]

    def validate(self, data):
        # checking if a fruit with the same name already exists
        fruit_name = data.get("name")
        if Fruit.objects.filter(name__iexact = fruit_name).exists():
            raise serializers.ValidationError({'name': f'A fruit with the name "{fruit_name}" already exists.'})
        return data

    def create(self, validated_data):
        vitamins = validated_data.pop('vitamins', []) 
        fruit = Fruit.objects.create(**validated_data)
        
        if vitamins:
            fruit.vitamins.set(vitamins)
            
        fruit.save()
        return fruit