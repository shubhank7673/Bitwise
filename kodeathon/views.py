from django.shortcuts import render
from django.http import HttpResponse
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
import string
from .models import kodeathon,livekod

def kodeathonf(request):
    kd = kodeathon.objects.all()
    if len(kd)==0:
        return HttpResponse('No upcoming kodeathons')
    kd = kd[len(kd)-1]
    if request.method == 'POST':
        if kd.TeamEvent==True:
            team = request.POST['teamname']
            member1 = request.POST['member1']
            member2 = request.POST['member2']
            member3 = request.POST['member3']
            mobile = request.POST['mobile']
            passwd = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
            scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('flowing-sign-237313-08e73b362c9a.json',scope)
            at = gspread.authorize(credentials)
            worksheet = at.open('teamregistration').sheet1
            worksheet.append_row([team,mobile,member1,member2,member3,passwd])
        else:
            name = request.POST['name']
            Er = request.POST['Er']
            email = request.POST['email']
            mobile = request.POST['mobile']
            passwd = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])
            scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('flowing-sign-237313-08e73b362c9a.json',scope)
            at = gspread.authorize(credentials)
            worksheet = at.open('individualregistration').sheet1
            worksheet.append_row([name,Er,mobile,passwd])
        return render(request,'success.html')
    if kd.isActive:
        return render(request,'kodeathon.html',{'name':kd.contestName,'TeamEvent':kd.TeamEvent})
    else:
        return render(request,'noUpcoming.html')
def live(request):
    kod = livekod.objects.all()
    if kod[0].isActive == False:
        return HttpResponse('<h1>No live kodeathons !</h1>')
    kod = kod[0]
    data = {'name':kod.name,'data':kod}
    return render(request,'live.html',data)
