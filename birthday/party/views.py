from django.shortcuts import render
from .models import Content

def index(request):
    # Get all content objects
    contents = Content.objects.all()
    
    # Define the carousel slides
    carousel_slides = [
        {'image': 'party/images/main_page_background.jpg', 'alt_text': 'Slide 1'},
        {'image': 'party/images/party2.jpg', 'alt_text': 'Slide 2'},
        {'image': 'party/images/party3.jpg', 'alt_text': 'Slide 3'},
    ]
    
    # Create the context dictionary with both contents and carousel slides
    context = {
        'Contents': contents,
        'carousel_slides': carousel_slides
    }
    
    # Render the template with the combined context
    return render(request, 'party/index.html', context)

def login_view(request):
    return render(request, 'party/login.html')

# create room 
def room_view(request):
    return render(request, 'party/room.html')