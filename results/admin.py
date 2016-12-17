from django.contrib import admin
from results.models import Student,Marks

# Register your models here.




class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'gender')
    list_filter = ('address', )
     
    readonly_fields = ['name'] 
     
    fieldsets = [
                           
        ('Perosnal Information', {
            'fields': [ 'name', 'age', 'gender' ],
        }),
        
        ('contact', {
            'fields': ['phone', 'address',],
        }),
        
    ]
admin.site.register(Student,StudentModelAdmin)
admin.site.register(Marks)