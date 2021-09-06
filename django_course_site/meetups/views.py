from django.shortcuts import render, redirect

from .models import MeetUp, Participant
from .forms import RegistrationForm

# Create your views here.
def index(request):
    meetups = MeetUp.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
        }
                )
    
def meetup_details(request, meetup_slug):
    try:
        selected_meetup = MeetUp.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        
        else:
            registration_form = RegistrationForm(request.POST)
            
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)
        
        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form,
            }
                        )
        
    except Exception as e:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False,
        }
                    )

def confirm_registration(request, meetup_slug):
    meetup = MeetUp.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email,
    })