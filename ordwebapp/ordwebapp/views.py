"""views to generate welcome page"""
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import WordForm

def welcome(request):
    """"view of the welcome page"""
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WordForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            selected_word_type = form.cleaned_data['word_class']
            request.session['selected_word_type'] = selected_word_type

            selected_level = form.cleaned_data['word_class']
            request.session['selected_level'] = selected_level
            # redirect to a new URL:
            return HttpResponseRedirect('/tarjetas/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WordForm()

    context = {
        'form': form,
    }

    return render(request, 'welcome.html', context)

def about(request):
    """"view of the about page"""
    return render(request, 'about.html')

def contact(request):
    """"view of the contact page"""
    return render(request, 'contact.html')
