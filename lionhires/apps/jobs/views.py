from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from linkedin import linkedin
from models import LinkedInUser

LINKED_IN_API_KEY = '77xwhoqz5szdvj'
LINKED_IN_SECRET = 'C2bnhwPZIKMTFIby'

def home(request):
  data = request.GET.copy()
  session = request.session
  if 'code' in data:
    request.session['auth_code'] = data['code']
    authentication = session['auth']
    authentication_code = data['code']
    authentication.authorization_code = authentication_code
    user_token = authentication.get_access_token()
    application = linkedin.LinkedInApplication(token=user_token)
    request.session['application'] = application
    user_data = application.get_profile(selectors = ['id', 'first-name', 'last-name'])
    if (len(LinkedInUser.objects.filter(linked_in_id = user_data['id'])) == 0):
      l = LinkedInUser.create(id = user_data['id'], first = user_data['firstName'], last = user_data['lastName'])
      l.save()
    return redirect("/profile/")
  else:
    authentication = linkedin.LinkedInAuthentication(LINKED_IN_API_KEY, LINKED_IN_SECRET, request.build_absolute_uri(), linkedin.PERMISSIONS.enums.values())
    request.session['auth'] = authentication
    return render_to_response('index.html', {'auth':authentication.authorization_url},
      context_instance=RequestContext(request))

def profile(request):
  session = request.session
  if 'application' in session:
    application = session['application']
    profile = application.get_profile(selectors = ['first-name', 'last-name', 'picture-url', 'headline'])
    c = {'first': profile['firstName'], 'last': profile['lastName'], 'photo': profile['pictureUrl'], 'headline':
      profile['headline']}
    return render_to_response('profile.html', c, context_instance=RequestContext(request))
  else:
    return redirect('/')

def logout(request):
  del request.session['application']
  return redirect('/')
    
