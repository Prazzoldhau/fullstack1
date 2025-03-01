from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render  # ✅ Import render function
from .models import SubmittedData
from django.http import HttpResponse

@csrf_exempt  # Disable CSRF for API requests
def home(request):
    return HttpResponse("Welcome to the Home Page!")  # Temporary home page

def submit_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON from Tkinter
            name = data.get('name')

            SubmittedData.objects.create(name=name)

            return JsonResponse({'status': 'success', 'message': 'Data saved successfully!'}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)



def view_data(request):
    data = SubmittedData.objects.all()  # Fetch submitted data

    return render(request, 'view_data.html', {'data': data})  # Pass data to template
