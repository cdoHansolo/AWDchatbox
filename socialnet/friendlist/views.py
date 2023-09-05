from django.shortcuts import render

# Create your views here.
def registration_view(request):
    return render(request, 'socialnet/registration_form.html')