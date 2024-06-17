from django.db import models

class Current_Status(models.Model):
    value = models.CharField(max_length=50)
    
    def __str__(self):
        return self.value

class User(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.IntegerField()
    nationality = models.IntegerField()
    identity_document = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income_modality = models.IntegerField()
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)    
    def __str__(self):
        return f"{self.income_modality} {self.monthly_income}"
       
class CreditDepartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_cost_department = models.DecimalField(max_digits=10, decimal_places=2)
    payment_initial = models.DecimalField(max_digits=10, decimal_places=2)
    payment_time = models.IntegerField()
    moving_time = models.IntegerField()
    has_department = models.BooleanField(default=False)
    profit_status = models.IntegerField()
    department_type = models.IntegerField()

    def __str__(self):
        return self.name

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_description = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)    

    def __str__(self):
        return f"{self.address_description}, {self.country}"
        
class ValidationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.code}"
    

class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_status = models.ForeignKey(Current_Status, on_delete=models.SET_NULL, null=True)
    salary_info = models.OneToOneField(Salary, on_delete=models.CASCADE, null=True)    
    credit_info = models.OneToOneField(CreditDepartment, on_delete=models.CASCADE, null=True)    
    address_info = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Form for {self.user.username}"    