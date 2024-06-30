from django.shortcuts import render, redirect
from . forms import MyForm
from . forms import modelClass

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = MyForm()

    return render(request, 'contact.html', {'form':form}) 

def model_form(request):
    if request.method == 'POST':
        model_class = modelClass(request.POST)
        if model_class.is_valid():
            model_class.save()
            return redirect("/first_app/model_form/")
    else:
        model_class = modelClass()
    return render(request, 'model_form.html', {'form':model_class})