from django.urls import path
from .views import home, submit_form, start_current_state, start_login, steps, verification_code, verify_code, base_lead_step

urlpatterns = [
    path('', home, name="home"),
    path('start_current_state', start_current_state, name="start_current_state"), 
    path('start_login', start_login, name="start_login"),    
    path('form', submit_form, name="submit_form"),
    path('steps/<int:option>/', steps, name="steps"),
    path('verification_code', verification_code, name ="verification_code"),
    path('verify_code', verify_code, name ="verify_code"),
    path('base_lead_step/<int:code>/', base_lead_step, name="base_lead_step"),
]