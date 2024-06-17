from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30, blank=True, null=True)
    last_name_paterno = models.CharField(max_length=30)
    last_name_materno = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    identity_document = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    

class Current_Status(models.Model):
    value = models.CharField(max_length=50)
    
    def __str__(self):
        return self.value

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Salary Model
class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.amount} {self.currency}"

# Address Model
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}"

# Personal Information Model
class PersonalInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# Email/Phone Validation Model
class ValidationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.code}"

# Credit Department Model
class CreditDepartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    credit_score = models.IntegerField()
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.credit_score}"    
    

# Forms Model (for collecting all form information)
class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_status = models.ForeignKey(Current_Status, on_delete=models.SET_NULL, null=True)
    department_info = models.OneToOneField(Department, on_delete=models.CASCADE, null=True)
    salary_info = models.OneToOneField(Salary, on_delete=models.CASCADE, null=True)
    address_info = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    personal_info = models.OneToOneField(PersonalInformation, on_delete=models.CASCADE, null=True)
    credit_info = models.OneToOneField(CreditDepartment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Form for {self.user.username}"    