from django.contrib import admin
from .models import EmpModel

# Register your models here.

class EmpModelAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
        model = EmpModel

admin.site.register(EmpModel, EmpModelAdmin)