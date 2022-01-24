from datetime import datetime


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib.auth.models import User

from prueba.models import Studient


@csrf_exempt
def index(request):
    if request.method == 'GET':
        s = Studient(name="Edu", birthday=datetime.now())
        s.save()
        return HttpResponse("Hello, world. You're at the polls index.")
    elif request.method == 'POST':
        data = json.loads(request.body)
        s = Studient(**data)
        users = User.objects.filter(username='eduardo')
        for u in users:
            print ('{} {} {} '.format(u.username, u.password, u.email))
        s.birthday = datetime.now()

        if Studient.objects.filter(name=s.name).exists():
            return HttpResponse("Existe")

        s.save()
        return HttpResponse("guardado.")
