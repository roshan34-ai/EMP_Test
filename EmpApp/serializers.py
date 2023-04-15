from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from . models import EmpModel, photob64

class empSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField()
    class Meta:
        fields = ('regid', 'name', 'email', 'age', 'gender', 'phoneNo', 'addressDetails', 'workExperience', 'qualifications', 'projects', 'photo')
        model = EmpModel

    def create(self, validated_data):
        if not validated_data.get('name'):
            raise serializers.ValidationError({"status":status.HTTP_400_BAD_REQUEST,
                                               "message":"name is required"})
        elif not validated_data.get('email'):
            raise serializers.ValidationError({"status":status.HTTP_400_BAD_REQUEST,
                                               "message":"email is required"})
        
        elif EmpModel.objects.filter(email=validated_data.get('email')).exists():
                raise serializers.ValidationError({"message":"employee with this email already exists.", 
                                                   "status":status.HTTP_200_OK
                                                   })
        elif not validated_data.get('age'):
            raise serializers.ValidationError({"status":status.HTTP_400_BAD_REQUEST,
                                               "message":"age is required"})
        elif not validated_data.get('gender'):
            raise serializers.ValidationError({"status":status.HTTP_400_BAD_REQUEST,
                                               "message":"gender is required"})
        elif not validated_data.get('phoneNo'):
            raise serializers.ValidationError({"status":status.HTTP_400_BAD_REQUEST,
                                               "message":"phoneNo is required"})
        elif not validated_data.get('addressDetails'):
            raise serializers.ValidationError({"status":status.HTTP_400_BAD_REQUEST,
                                               "message":"addressDetails is required"})
        elif not validated_data.get('workExperience'):
            raise serializers.ValidationError({"status":status.HTTP_400_BAD_REQUEST,
                                               "message":"workExperience is required"})
        elif not validated_data.get('qualifications'):
            raise serializers.ValidationError({"status":status.HTTP_400_BAD_REQUEST,
                                               "message":"qualification is required"})
        elif not validated_data.get('projects'):
            raise serializers.ValidationError({"status":status.HTTP_400_BAD_REQUEST,
                                               "message":"projects is required"})
        elif not validated_data.get('photo'):
            raise serializers.ValidationError({"status":status.HTTP_400_BAD_REQUEST, 
                                               "message":"photo is required"})
        empObj = EmpModel.objects.create(
                                name=validated_data.get('name'),
                                email=validated_data.get('email'),
                                age=validated_data.get('age'),
                                gender=validated_data.get('gender'),
                                phoneNo=validated_data.get('phoneNo'),
                                addressDetails=validated_data.get('addressDetails'),
                                workExperience=validated_data.get('workExperience'),
                                qualifications=validated_data.get('qualifications'),
                                projects=validated_data.get('projects'),
                                photo = photob64(validated_data.get('photo'))
                    )
        return empObj
    
class empReadSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('regid', 'name', 'email', 'age', 'gender', 'phoneNo', 'addressDetails', 'workExperience', 'qualifications', 'projects', 'photo')
        model = EmpModel
