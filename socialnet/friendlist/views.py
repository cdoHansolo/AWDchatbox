from django.shortcuts import render, redirect
from.forms import RegistrationForm

# Create your views here.
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save() #Save the user and log in
        return redirect('registration_success') #Redirect to a success page
    else:
        form = RegistrationForm()

    return render(request, 'socialnet/registration_form.html', {'form':form})