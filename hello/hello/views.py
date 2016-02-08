from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Template, Context
from django.shortcuts import render
import datetime

def hello(request):
    now = datetime.datetime.now()
#    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
#    fp = open('/v/global/user/z/za/zakhark/django/hello/hello/templates/mytemplate.html')
#    t = Template(fp.read())
#    t = get_template('mytemplate.html')
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)
#    return HttpResponse("Hello world")
    return render(request, 'mytemplate.html', {'current_date': now})

def abascript(request):
	new_file = '/v/global/user/z/za/zakhark/ABAdownload.sh'
	f = open(new_file, 'r')
	script=f.read()
	return HttpResponse(script, content_type='text/plain')


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
