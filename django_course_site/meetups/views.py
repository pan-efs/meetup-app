from django.shortcuts import render

from .models import MeetUp

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
        
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup_title': selected_meetup.title,
            'meetup_description': selected_meetup.description
        }
                    )
    except Exception as e:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False,
        }
                    )