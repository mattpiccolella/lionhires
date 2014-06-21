from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
  data = request.GET.copy();
  if 'code' in data:
    return HttpResponse(data['code'])
  else:
    return render_to_response('index.html', c)
