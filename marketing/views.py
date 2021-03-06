import json
import datetime
from django.utils import timezone
from django.shortcuts import render, HttpResponse
from django.conf import settings
# Create your views here.

def dismiss_marketing_message(request):
	if request.is_ajax():
		data = {}
		print(data)
		json_data = json.dumps(data)
		request.session['dismiss_message_for'] = str(timezone.now()+ datetime.timedelta(hours=settings.MARKETING_HOURS_OFFSET, seconds=settings.MARKETING_SECONDS_OFFSET))
		print(json_data)
		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404

