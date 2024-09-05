from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm, ProfileForm, FatherProfileForm
from django.forms import formset_factory
from django.contrib.auth.decorators import login_required


# Create your views here.

def ProfileListView(request):
    profiles = Profile.objects.all()
    user = request.user
    return render(request, 'matrimony/profile_list.html', {'profiles': profiles, 'user': user})

def ProfileDetailView(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    user = request.user
    return render(request, 'matrimony/profile_detail.html', {'profile': profile, 'user': user})

@login_required
def ProfileDeleteView(request, profile_id):
    profile=Profile.objects.get(id=profile_id)
    profile.delete()
    return redirect ('matrimony:profile_list')

def ContactView(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print(f"NAME: {form.cleaned_data['name']}")
            print(f"EMAIL: {form.cleaned_data['email']}")
            print(f"MESSAGE: {form.cleaned_data['message']}")
    else:
        form = ContactForm()

    user = request.user
    return render(request, 'matrimony/contact.html', {'form': form, 'user': user})


@login_required
def ProfileFormView(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('matrimony:profile_list')
    else:
        form = ProfileForm()

    return render(request, 'matrimony/new_profile.html', {'form': form})


@login_required
def FatherProfileView(request):

    if request.method == 'POST':
        form = FatherProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('matrimony:profile_list')
    else:
        form = FatherProfileForm()

    return render(request, 'matrimony/father_profile.html', {'form': form})
 