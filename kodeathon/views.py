from django.shortcuts import render
from django.http import HttpResponse
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import string
from .models import kodeathon

def kodeathonf(request):
    kd = kodeathon.objects.all()
#     print (kd)
#     print (len(kd))
    if len(kd)==0:
        return HttpResponse('No upcoming kodeathons')
    kd = kd[len(kd)-1]
    if request.method == 'POST':
        team = request.POST['teamname']
        member1 = request.POST['member1']
        member2 = request.POST['member2']
        member3 = request.POST['member3']
        passwd = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('flowing-sign-237313-08e73b362c9a.json',scope)
        at = gspread.authorize(credentials)
        worksheet = at.open(kd.sheetName).sheet1
        worksheet.append_row([team,member1,member2,member3,passwd])
        return HttpResponse('registration successfull<br><a href="http://bitwisejuet.pythonanywhere.com">Click here</a> to return to main site')
    if kd.isActive:
        return render(request,'kodeathon.html',{'name':kd.contestName})
    else:
        return HttpResponse('No upcoming kodeathons')
