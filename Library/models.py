from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    qty = models.IntegerField()
    price = models.FloatField()
    author = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "book1"  # give name of table to creat


# class BookForm(models.Model): # django create form
#     name = models.CharField(max_length = 200)
#     age = models.IntegerField()
#     mobile_num = models.IntegerField()
#     address = models.CharField(max_length = 200)
#     email = models.EmailField(null=True)

#     def _str_(self):
#         return self.name

#     class Meta:
#         db_table = "form"



# -------------------------------------------
#  relation model        # 

# class CommonName(models.Models):
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name
    
# class College(CommonName):
#     address = models.CharField(max_length=100)
    
#     class Meta():
#         db_table = "college"
        
# class Principal(CommonName):
#     exp = models.FloatField()
#     edu = models.CharField(max_length=100)
#     College = models.OneToOneField(College, on_delete= models.CASCADE, related_name="principal")
#                                                                                     # class_name
#     class Meta():
#         db_table = "principal"
        
# class Department(CommonName):
#     branch = models.CharField(max_length=100)
#     lib = models.CharField(max_length=100)
#     College = models.ForeignKey(College, on_delete=models.CASCADE, related_name="department")
        
#     class Meta():
#         db_table = "department"
        
# class Student(CommonName):
#     stud_strngth = models.CharField(max_length=100)
#     stud_age = models.CharField(max_length=100)
#     Department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="student")
    
#     class Meta():
#         db_table = "student"
        
# class Subject(CommonName):
#     prac_sub = models.CharField(max_length=100)
#     theory_sub = models.CharField(max_length=100)
#     Department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="subject")    
    
#     class Meta():
#         db_table = "subject"
    
   