from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def start_current_state(request):
    return render(request, 'current_State.html')
    
def start_login(request):
    return render(request, 'login.html')
    
def submit_form(request):
    if request.method == 'POST':
        return redirect("success_page")
    return render(request, 'default.html')      

def steps(request, option):
    context = {'option': option}
    if option == 1:
        return render(request, 'step1.html', context)
    elif option == 2:
        return render(request, 'step2.html', context)
    elif option == 3:        
        return render(request, 'step3.html', context)
    elif option == 4:        
        return render(request, 'step4.html', context)

def verification_code(request):
    usuario = "jorge.villavicencio10@gmail.com"
    context = {
        'usuario': usuario
    }
    return render(request, 'verification_code.html', context)    

def verify_code(request):
    user_name = "Jorge"
    context = {
        'user_name': user_name
    }
    return render(request, "potential_lead_step1.html", context)

def base_lead_step(request, code):

    user_name = "Jorge"
    context = {
        'user_name': user_name
    }    
    if code == 1:
        return render(request, 'potential_lead_step1.html', context)
    elif code == 2:
        return render(request, 'potential_lead_step2.html', context)
    elif code == 3:        
        return render(request, 'potential_lead_step3.html', context)
    elif code == 4:        
        return render(request, 'potential_lead_step4.html', context)
    elif code == 5:        
        return render(request, 'potential_lead_step5.html', context)
    elif code == 6:        
        return render(request, 'potential_lead_step6.html', context)                        
    elif code == 7:        
        return render(request, 'potential_lead_step7.html', context)         


