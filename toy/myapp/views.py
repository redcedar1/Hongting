from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Info
from myproject import settings
import requests
from django.template import loader
from django.http import HttpResponse, JsonResponse

# Create your views here.
  
count = 0

def index(request):
    return render(request, 'myapp/index.html')


def kakaologin(request):
    context = {'check':False}
    if request.session.get('access_token'): #만약 세션에 access_token이 있으면(==로그인 되어 있으면) 
        context['check'] = True #check 가 true, check는 kakaologin.html내에서 if문의 인자
    return render(request,"myapp/kakaologin.html",context)

def kakaoLoginLogic(request):
    _restApiKey = '7357a0ebc5b601b560b1475e76d898de' # 입력필요
    _redirectUrl = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = '7357a0ebc5b601b560b1475e76d898de' # 입력필요
    _redirect_uri = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    return render(request, 'myapp/loginsuccess.html')

def kakaoLogout(request):
    _token = request.session['access_token']
    _url = 'https://kapi.kakao.com/v1/user/logout'
    _header = {
      'Authorization': f'bearer {_token}'
    }
    # _url = 'https://kapi.kakao.com/v1/user/unlink'
    # _header = {
    #   'Authorization': f'bearer {_token}',
    # }
    _res = requests.post(_url, headers=_header)
    _result = _res.json()
    if _result.get('id'):
        del request.session['access_token']
        return render(request, 'myapp/loginoutsuccess.html')
    else:
        return render(request, 'myapp/logouterror.html')




def home(request):
    article = 'home is here'
    context = {"article":article}
    return render(request, "myapp/home.html", context)

@csrf_exempt
def meeting(request):
    global count
    if request.method == "POST": # /home/meeting페이지로 인원 선택한 정보 전달
        peoplenum = ''
        peoplenum = request.POST.get('submit_peoplenum') #인원 선택 정보 추출
        if peoplenum is None: #인원 값이 없으면
            errormsg = {"error_message": "인원을 선택하지 않으셨습니다."}
            return render(request, "myapp/meeting.html", errormsg)
        q = Info.objects.create(peoplenums=peoplenum)
        q.save()
        count = q.id
        print(count)
        return redirect("/meeting2")# /home/meeting2로 페이지 전달
    return render(request, "myapp/meeting.html")


@csrf_exempt
def meeting2(request):
    global count
    if request.method == "POST": # /home/meeting2 로 선호 직업, 장소, 나이 전달
        job = request.POST.get('submit_job')
        location = request.POST.get('submit_location')
        age = request.POST.get('submit_age')

        q = Info.objects.latest('id')
        q.jobs = job
        q.locations = location
        q.ages = age
        q.save()
        return redirect("/home/")

    count += 1
    return render(request, "myapp/meeting2.html")

def alonechoose(request):

    return render(request, "myapp/alonechoose.html")

def alonechoose2(request):

    return render(request, "myapp/alonechoose2.html")

def army(request):

    return render(request, "myapp/army.html")

def body(request):

    return render(request, "myapp/body.html")

def eyes(request):

    return render(request, "myapp/eyes.html")

def height(request):

    return render(request, "myapp/height.html")

def hobby(request):

    return render(request, "myapp/hobby.html")

def kakao(request):

    return render(request, "myapp/kakao.html")

def major(request):

    return render(request, "myapp/major.html")

def mbti(request):

    return render(request, "myapp/mbti.html")

def myinfo(request):
    access_token = request.session.get("access_token")
    account_info = requests.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"}).json()
    email = account_info.get("kakao_account", {}).get("email") # email이 있으면 email반환 없으면 빈칸 반환
    nickname = account_info.get("kakao_account", {}).get("nickname")
    context = {'email' : email, 'nickname':nickname}
    return render(request, "myapp/myinfo.html",context)

def success(request):

    return render(request, "myapp/success.html")

def youinfo(request):

    return render(request, "myapp/youinfo.html")


def my(request):

    return render(request, "myapp/my.html")
    
'''
이런 방식을 사용해도 된다
def my(request):
    article = 'my'
    template = loader.get_template(myapp/my.html)
    context = {"article":article}
    return HttpResponse(template.render(context,request))

'''
def you(request):
    article = 'you'
    context = {"article":article}
    return render(request, "myapp/you.html", context)


def choose(request):

    return render(request, "myapp/choose.html")
      
def matching(request):
    article = 'matching'
    context = {"article":article}
    return render(request, "myapp/matching.html", context)
    

def result(request):
    article = 'result'
    context = {"article":article}
    return render(request, "myapp/result.html", context)
    

def menu(request):
    article = 'menu'
    context = {"article":article}
    return render(request, "myapp/menu.html", context)
    