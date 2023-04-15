from django.db import models
import base64

# Function to create custome id
def create_id():
    try:
        obj = EmpModel.objects.last()
        regid = int(obj.regid[3:])
        regid+=1
        regid = "EMP00"+str(regid)
        return regid
    except :
        regid = "EMP001"
        return regid
    
# Create your models here.
class EmpModel(models.Model):
    regid = models.CharField(primary_key=True, unique=True, default=create_id, editable=False, max_length=10)
    name=models.CharField(max_length=100, blank=True, null=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    age=models.IntegerField(blank=True, null=True)
    gender=models.CharField(max_length=100, blank=True, null=True)
    phoneNo=models.CharField(max_length=100, blank=True, null=True)
    addressDetails=models.CharField(max_length=100, blank=True, null=True)
    workExperience=models.CharField(max_length=100, blank=True, null=True)
    qualifications=models.CharField(max_length=100, blank=True, null=True)
    projects=models.CharField(max_length=100, blank=True, null=True)
    photo=models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.regid
    
# Function to covert image into base64 str
def photob64(data):
    my_string = base64.b64encode(data.read())
    return my_string
