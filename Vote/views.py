from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
import pyotp
import base64
from django.views import generic
from django.utils import timezone
from django.urls import reverse
from django.utils.http import  urlsafe_base64_encode
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User




from .models import Polls, Choice, User, AbstractUser, VOTED
#from .forms import PollsForm, ChoiceForm

# Create your views here.
class generateKey:
    @staticmethod
    def returnValue(email):
        return str(email) + str(datetime.date(datetime.now())) + "OUOUOO#EVOTE"

def getotp(request, user):
    if request.method == 'POST':
        user = User.objects.get(first_name=user)
        email = user.email
        Mobile = User.objects.get(email=email)
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(email).encode())
        OTP = pyotp.HOTP(key)
        if OTP.verify(request.POST.get("otp"), user.count):

            login(request, user)
            return redirect('Vote:index')
        else:
            print('wrong token')
    else:
        user = User.objects.get(first_name=user)
        email = user.email
        context = {'user': user}
        user.count += 1
        user.save()
        Mobile = User.objects.get(email=email)  # if Mobile already exists the take this else create New One
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(email).encode())  # Key is generated
        OTP = pyotp.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(user.count))
    # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
    return render(request, 'Vote/getotp.html', context)

def sendotp(request, user):
    user = User.objects.get(first_name=user)
    context = {'user': user}
    return render(request, 'Vote/sendotp.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Vote:index')
    else:
        if request.method == 'POST':

            username = request.POST.get('username')

            user = authenticate(request, username=username)

            if user is not None:
                #login(request, user)

                return redirect('Vote:sendotp', user)
            else:
                print('incorrect')
                messages.info(request, 'Username or Password is incorrect')
        return render(request, 'Vote/login.html')

def logoutUser(request):
    logout(request)
    return redirect('Vote:login')

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'Vote/index.html'
    context_object_name = 'Available_polls'

    def get_context_data(self, **kwargs):
        #pk = self.kwargs['pk']
        context = super(IndexView, self).get_context_data(**kwargs)

        context['sug'] = Polls.objects.filter(Type='SUG')
        context['faculty'] = Polls.objects.filter(Category=self.request.user.Faculty)
        return context


    def get_queryset(self):
        return Polls.objects.filter(Category=self.request.user.Dept)



@method_decorator(login_required, name='dispatch')
class DeptDetailView(generic.DetailView):
    model = Polls
    template_name = 'Vote/Deptvote.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        poll = Polls.objects.get(id=pk)
        context = super().get_context_data(**kwargs)
        #context = super(DeptDetailView, self).get_context_data(**kwargs)
        try:
            context['voted'] = VOTED.objects.get(has_voted=poll, user_voted=self.request.user, Voted=True)
        except (KeyError, VOTED.DoesNotExist):
            return context
        else:
            return context

    #def get_queryset(self):
     #   return Polls.objects.all()


@method_decorator(login_required, name='dispatch')
class DeptView(generic.ListView):
    context_object_name = 'Dept_polls'
    template_name = 'Vote/dept.html'


    def get_queryset(self):
        return Polls.objects.filter(Category=self.request.user.Dept)

@method_decorator(login_required, name='dispatch')
class FacultyView(generic.ListView):
    context_object_name = 'Faculty_polls'
    template_name = 'Vote/faculty.html'

    def get_queryset(self):
        return Polls.objects.filter(Category=self.request.user.Faculty)


@method_decorator(login_required, name='dispatch')
class SUGView(generic.ListView):
    context_object_name = 'SUG_polls'
    template_name = 'Vote/sug.html'

    def get_queryset(self):
        return Polls.objects.filter(Type='SUG')


@method_decorator(login_required, name='dispatch')
class ResultsView(generic.DetailView):
    model = Polls
    template_name = 'Vote/results.html'


@login_required(login_url='login')
def vote(request, poll_id):
    polls = get_object_or_404(Polls, pk=poll_id)
    poll = Polls.objects.get(id=poll_id)
    user = request.user
    try:
        voted = VOTED.objects.get(has_voted=poll, user_voted=user, Voted=True)
        #voted = VOTED.objects.filter(has_voted_id=poll_id)
    except (KeyError, VOTED.DoesNotExist):
        Uservoted = VOTED.objects.create(has_voted=poll, user_voted=user, Voted=False)
        try:
            selected_choice = polls.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'Vote/DeptVote.html', {
                'polls': polls,
                'error_message': "You didn't select a choice.",
            })

        else:
            selected_choice.votes += 1
            selected_choice.save()
            Uservoted.Voted = True
            Uservoted.save()
            return HttpResponseRedirect(reverse('Vote:deptdetail', args=(polls.id,)))
    else:
        print(voted.user_voted.first_name)
        return render(request, 'Vote/Deptvote.html', {
            'polls': polls,
            'error_message':'Sorry You can only vote once',
        })
