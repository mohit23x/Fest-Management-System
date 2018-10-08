from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from .models import Event, Sponser
from .forms import EventForm, UserCreateForm, addcoordinatortoevenntForm, addsponserForm
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test


users_in_group = Group.objects.get(name="ORGANIZERS").user_set.all()
users_in_group2 = Group.objects.get(name="COORDINATOR").user_set.all()


@login_required
def maindashboard(request):
    if request.user in users_in_group:
        sdata = Sponser.objects.all()
        edata = Event.objects.all()
        return render(request, 'pages/maindashboard.html', {'sdata': sdata, 'edata': edata})
    elif request.user in users_in_group2:
        sdata = Sponser.objects.all()
        edata = Event.objects.all()
        return render(request, 'student/maindashboard.html', {'sdata': sdata, 'edata': edata})
    else:
        return HttpResponse('something is wrong wth your credentials, please login again')

def allevents(request):
    if request.user in users_in_group:
        data = Event.objects.all()
        return render(request, 'pages/allevents.html', {'data': data})
    elif request.user in users_in_group2:
        data = Event.objects.all()
        return render(request, 'student/allevents.html', {'data': data})
    else:
        return HttpResponse('something is wrong wth your credentials, please login again')


def addevent(request):
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            minimumparticipant = form.cleaned_data['minimumparticipant']
            maximumparticipant = form.cleaned_data['maximumparticipant']
            date = form.cleaned_data['date']
            entries = form.cleaned_data['entries']
            fees = form.cleaned_data['fees']

            Event.objects.create(
                name=name,
                description=description,
                minimumparticipant=minimumparticipant,
                maximumparticipant=maximumparticipant,
                date=date,
                entries=entries,
                fees=fees
            ).save()

        return redirect('allevents')

    else:
        form = EventForm()

    return render(request, 'pages/addevent.html', {'form': form})

def allcoordinators(request):
    if request.user in users_in_group:

        data = Event.objects.all()
        return render(request, 'pages/allcoordinators.html', {'data':data})
    elif request.user in users_in_group2:
        data = Event.objects.all()
        return render(request, 'student/allcoordinators.html', {'data': data})


class addcoordinator(View):
    form_class = UserCreateForm
    template_name = 'pages/addcoordinators.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #clean normalised data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #            user.groups.add(Group.objects.get(name='COORDINATOR'))
            user.set_password(password)
            user.save()
            usr = User.objects.get(username=username)
            usr.groups.add(Group.objects.get(name='COORDINATOR'))
            usr.save()

            return redirect('addcoordin')
            '''user = authenticate(username=   username, password= password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('addcoordin')'''
        return render(request, self.template_name, {'form': form})





def sponsers(request):
    if request.user in users_in_group:

        sponser = Sponser.objects.all()
        return render(request, 'pages/sponsers.html', {'sponser':sponser})

    elif request.user in users_in_group2:
        sponser = Sponser.objects.all()
        return render(request, 'student/sponsers.html', {'sponser': sponser})


def addcoordin(request):
    if request.user in users_in_group:
        data = User.objects.all()
        return render(request, 'pages/addcoordin.html', {'data':data})
    elif request.user in users_in_group2:
        data = User.objects.all()
        return render(request, 'student/addcoordin.html', {'data': data})


def eventdelete(request, pk):
    if request.user in users_in_group:
        Event.objects.get(pk=pk).delete()
        return redirect('allevents')


def addcoordinatortoevennt(request, pk):
    if request.method == 'POST':
        form = addcoordinatortoevenntForm(request.POST)

        if form.is_valid():

            obj = Event.objects.get(pk=pk)
            obj.user.set(form.cleaned_data['user'])
            obj.save()

            return redirect('allcoordinators')

    else:
        form = addcoordinatortoevenntForm()

    return render(request, 'pages/addcoordinatortoeventform.html',{'form': form})




def addsponser(request):
    if request.method ==  'POST':
        form = addsponserForm(request.POST)
        if form.is_valid():

            name= form.cleaned_data['name']
            address = form.cleaned_data['address']
            website= form.cleaned_data['website']
            contact= form.cleaned_data['contact']
            amount= form.cleaned_data['amount']

            Sponser.objects.create(
                name=name,
                address = address,
                website = website,
                contact = contact,
                amount = amount
            ).save()

            return redirect('sponsers')

    else:
        form = addsponserForm()

    return render(request, 'pages/addsponserform.html', {'form': form})


def positive(request, pk):
    pos = Sponser.objects.get(pk=pk)
    poss = pos.positive
    poss = poss + 1
    pos.positive = poss
    pos.save()
    return redirect('sponsers')

def negative(request, pk):
    pos = Sponser.objects.get(pk=pk)
    poss = pos.negative
    poss = poss - 1
    pos.negative = poss
    pos.save()
    return redirect('sponsers')

def final(request, pk):
    pos = Sponser.objects.get(pk=pk)
    poss = pos.positive
    poss = 99
    pos.positive = poss
    pos.save()
    pos.final = True
    pos.save()
    return redirect('sponsers')


def removesponser(request, pk):
    pos = Sponser.objects.get(pk=pk).delete()
    return redirect('sponsers')


'''def addcoordinators(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            group = form.cleaned_data['group']
            user = authenticate(username=username, password=password)

            login(request, user)
            return HttpResponseRedirect('/maindashboard')
    else:
        form = UserCreateForm()

    return render(request, 'pages/addcoordinators.html', {'form': form})'''
