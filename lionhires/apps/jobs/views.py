from django.http import HttpResponse
from django.shortcuts import render_to_response
from linkedin import linkedin

LINKED_IN_API_KEY = '77xwhoqz5szdvj'
LINKED_IN_SECRET = 'C2bnhwPZIKMTFIby'

def home(request):
  data = request.GET.copy();
  if 'code' in data:
    return HttpResponse("Redirect works!")
  else:
    authentication = linkedin.LinkedInAuthorization(API_KEY, API_SECRET, request.build_absolute_uri(), linkedin.PERMISSIONS.enums.values())
    return HttpResponse(authentication.authorization_url)    
    
