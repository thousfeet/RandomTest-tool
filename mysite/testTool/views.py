import base64
from datetime import datetime

from django.contrib.sites import requests
from django.shortcuts import render, get_object_or_404
from .models import students
from Crypto.Cipher import DES


def index(request):
    return render(request, 'index.html')


def confirm_action(request):
    stu_id = request.POST['stuId']
    student = get_object_or_404(students, stuId=stu_id)
    student2 = students.objects.get(pk=student.matchId)
    return render(request, 'submit_page.html', {'student': student, 'student2': student2})


def submit_page(request):
    stu_id = request.POST['stu_id']
    score = request.POST['score']
    reason = request.POST['reason']
    student = get_object_or_404(students, stuId=stu_id)
    student2 = students.objects.get(pk=student.matchId)
    if score is not None and 0 <= int(
            score) <= 15 and reason is not None and student2.score is None and student2.reason is None:
        student2.score = score
        student2.reason = reason
        student2.save()
    return render(request, 'successful_page.html')

##################################


class Jwt:
    def __init__(self, xh, pwd):
        self.xh = xh
        self.pwd = pwd

    token = ''
    key = 'n&1P)J^A'
    iv = 'n&1P)J^A'

    def login(self):

        data = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        para = {"xh": self.xh, 'pwd': self.pwd, 'connect': '000000-000000-0000000-000000', 'date': data,
                'methodType': 'stulogin', 'machine': 'fuckyou', '22appVersionCode': 'fuckyou'}
        x = requests.post("http://59.77.134.232/fzuapp/UserHandler.ashx", data=para).text
        self.token = self.des_ecrypt(self.xh + '_' + data + '_' + self.getSeed(self.xh, data))
        print(x)
        return True

    '''
    YYYYMMDDhhmmss
    %Y%m%d%H%M%S
      body: `xh=${xh}&date=${dateStr}&methodType=stulogin&machine=%7B%22appVersionCode%22%3A4%2C%22appVersionName%22%3A%221.2.2%22%2C%22osVersion%22%3A%226.0.1%22%2C%22phoneModel%22%3A%22VMware+Virtual+Platform%22%2C%22sdkVersion%22%3A23%7D&pwd=${password}&connect=`
      const str = `${xh}_${dateStr}_${getSeed(xh, dateStr)}`;
    '''

    def getSeed(self, string, substring):
        substring2 = substring[0:4]
        substring3 = substring[4:6]
        substring4 = substring[6:8]
        substring5 = substring[8:10]
        substring6 = substring[10:12]
        substring = substring[12:14]
        i = int(string) % 63 + 1
        string = ""
        n = 0
        while i > 0:
            if i % 2 != 0:
                string = [substring2, substring3, substring4, substring5, substring6, substring][n] + string
            n += 1
            i >>= 1
        return string

    @classmethod
    def des_ecrypt(cls, ecryptText):
        cipherX = DES.new(cls.key, DES.MODE_CBC, cls.iv)
        pad = 8 - len(ecryptText) % 8
        padStr = ""
        for i in range(pad):
            padStr += chr(pad)
        ecryptText = ecryptText + padStr
        ecrypt_str = cipherX.encrypt(ecryptText)
        return base64.b64encode(ecrypt_str).decode()
