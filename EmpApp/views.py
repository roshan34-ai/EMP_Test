from rest_framework.response import Response
from .models import EmpModel, photob64
from rest_framework import status
from .serializers import empSerializer, empReadSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class empViewSet(ModelViewSet):
    queryset=EmpModel.objects.all()
    serializer_class=empSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['regid', 'email']
    http_method_names=['get', 'post', 'head', 'put', 'delete']

    # Get the list of all employees
    def list(self, request, *args, **kwargs):
        Queryset = self.queryset
        if Queryset:
            serializer = empReadSerializer(Queryset, many=True)
            return Response({
                    "message":"employee details found",
                    "status":status.HTTP_200_OK,
                    "success":True,
                    "data":serializer.data
                })
        return Response({
            "message":"employee details not found",
            "status":status.HTTP_200_OK,
            "success":False,
        })

    # Get a single object of employee based on their regid
    def retrieve(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                Queryset = self.queryset.get(regid=kwargs.get('pk'))
                serializer=empReadSerializer(Queryset)
                return Response({
                        "message":"employee details found",
                        "status":status.HTTP_200_OK,
                        "success":True,
                        "data":serializer.data
                        })
            except:
                return Response({
                            "message":"employee details not found",
                            "status":status.HTTP_200_OK,
                            "success":False
                        })
        return Response({
                    "message":"employee details not found",
                    "status":status.HTTP_200_OK,
                    "success":False,
                    
                    })


    # Update employee details  
    def update(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            try:
                Queryset = self.queryset.get(regid=kwargs.get('pk'))
                serializer = self.serializer_class(Queryset, data=request.data )
                if serializer.is_valid(raise_exception=True):
                    Queryset.name = serializer.validated_data.get('name')
                    Queryset.email = serializer.validated_data.get('email')
                    Queryset.age = serializer.validated_data.get('age')
                    Queryset.gender = serializer.validated_data.get('gender')
                    Queryset.phoneNo = serializer.validated_data.get('phoneNo')
                    Queryset.addressDetails = serializer.validated_data.get('addressDetails')
                    Queryset.workExperience = serializer.validated_data.get('workExperience')
                    Queryset.qualifications = serializer.validated_data.get('qualifications')
                    Queryset.projects = serializer.validated_data.get('projects')
                    Queryset.photo = photob64(serializer.validated_data.get('photo'))
                    Queryset.save()
                    return Response({
                                    "message":"employee details updated successfully",
                                    "status":status.HTTP_200_OK
                                })
            except:
                return Response({
                        "message":"no employee found with this regid",
                        "status":status.HTTP_200_OK
                        })

        return Response({
            "message":"employee updation failed",
            "status":status.HTTP_400_BAD_REQUEST
        })

    # delete employee details
    def destroy(self, request, *args, **kwargs):
        if kwargs.get('pk'):
            try:
                obj = EmpModel.objects.get(regid=kwargs.get('pk'))
                obj.delete
                return Response({
                    "message":"employee deleted successfully",
                    "status":status.HTTP_200_OK,
                    "success":True
                    })
            except:
                return Response({
                        "message":"no employee found with this regid",
                        "status":status.HTTP_200_OK,
                        "success":False
                        })
        return Response({
            "message":"employee deletion faild",
            "success":False
            })