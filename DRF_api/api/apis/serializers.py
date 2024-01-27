from rest_framework import serializers
from django.contrib.auth.models import User
from .models import * 

class user_ser(serializers.ModelSerializer): 
    
    class Meta: 
        model = User 
        fields = ['username', 'password']
    
    def create(self, validated_data): 
        user = User.objects.create(username = validated_data['username']) 
        user.set_password(validated_data['password'])
        user.save()
        return user 
    

class student_ser(serializers.ModelSerializer): 
    class Meta: 
        model = Student 
        fields = '__all__'

    def validate(self, data): 
        if data['age'] < 18: 
            raise serializers.ValidationError({'error': 'Age must be equal or greater than 18'})

        if data['name']: 
            for i in data['name']: 
                if i.isdigit(): 
                    raise serializers.ValidationError({'error': 'Name cannot be numeric'})
        return data  
    

class category_ser(serializers.ModelSerializer): 
    class Meta: 
        model = Category 
        fields = '__all__'

class book_ser(serializers.ModelSerializer): 
    category = category_ser()
    class Meta: 
        model = Book
        fields = '__all__'
        # depth = 1


