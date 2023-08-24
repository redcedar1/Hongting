from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Info
from myproject import settings
import requests
from django.template import loader
from django.http import HttpResponse, JsonResponse

# Create your views here.
  
count = 0
@csrf_exempt
def index(request):
   return render(request, 'myapp/index.html')



def kakaologin(request):
    context = {'check':False}
    if request.session.get('access_token'): #만약 세션에 access_token이 있으면(==로그인 되어 있으면)
        return redirect("/meeting/") #check 가 true, check는 kakaologin.html내에서 if문의 인자

    return render(request,"myapp/kakaologin.html",context)

def kakaoLoginLogic(request):
    _restApiKey = '60010e5242c371826d538b43def648c3' # 입력필요
    _redirectUrl = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/authorize?client_id={_restApiKey}&redirect_uri={_redirectUrl}&response_type=code'
    return redirect(_url)

def kakaoLoginLogicRedirect(request):
    _qs = request.GET['code']
    _restApiKey = '60010e5242c371826d538b43def648c3' # 입력필요
    _redirect_uri = 'http://127.0.0.1:8000/kakaoLoginLogicRedirect'
    _url = f'https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={_restApiKey}&redirect_uri={_redirect_uri}&code={_qs}'
    _res = requests.post(_url)
    _result = _res.json()
    print()
    print(_result)
    print()
    request.session['access_token'] = _result['access_token']
    request.session.modified = True
    
    return redirect("/meeting")

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
    
    print(_result.get('id'))#액세스 토큰은 바뀌어도 id값은 안바뀌니 이것으로 조회 가능
    if _result.get('id'):
        
        del request.session['access_token']
        return render(request, 'myapp/loginoutsuccess.html')
    else:
        return render(request, 'myapp/logouterror.html')


@csrf_exempt
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
        if peoplenum == '': #인원 값이 없으면
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
        print(job)
        print(location)
        print(age)

        if job == '' or location =='': #인원 값이 없으면
            errormsg = {"error_message": "모든 필드에서 최소 한가지를 선택해 주세요."}
            return render(request, "myapp/meeting2.html", errormsg)

        q = Info.objects.latest('id')
        q.jobs = job
        q.locations = location
        q.ages = age
        q.save()
        return redirect("/home/")

    count += 1
    return render(request, "myapp/meeting2.html")
@csrf_exempt
def alonechoose(request):

    return render(request, "myapp/alonechoose.html")
@csrf_exempt
def alonechoose2(request):

    return render(request, "myapp/alonechoose2.html")
@csrf_exempt
def army(request):

    return render(request, "myapp/army.html")
@csrf_exempt
def body(request):

    return render(request, "myapp/body.html")
@csrf_exempt
def eyes(request):

    return render(request, "myapp/eyes.html")
@csrf_exempt
def height(request):

    return render(request, "myapp/height.html")
@csrf_exempt
def hobby(request):

    return render(request, "myapp/hobby.html")
@csrf_exempt
def kakao(request):

    return render(request, "myapp/kakao.html")
@csrf_exempt
def major(request):

    return render(request, "myapp/major.html")
@csrf_exempt
def mbti(request):

    return render(request, "myapp/mbti.html")

myinfo_arr = {}
@csrf_exempt
def myinfo(request):
    access_token = request.session.get("access_token")
    account_info = requests.get("https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"}).json()
    email = account_info.get("kakao_account", {}).get("email") # email이 있으면 email반환 없으면 빈칸 반환
    nickname = account_info.get("kakao_account", {}).get("nickname")
    context = {'email' : email, 'nickname':nickname}
    context.update(myinfo_arr)
    print(email)
    print(nickname)
    
    return render(request, "myapp/myinfo.html",context)
@csrf_exempt
def success(request):

    return render(request, "myapp/success.html")
@csrf_exempt
def youinfo(request):

    return render(request, "myapp/youinfo.html")

@csrf_exempt
def my(request,id):
    global myinfo_arr
    index = int(id) + 1
    if request.method == "POST":
        if int(id) == 1:
            age = request.POST.get("age")
            myinfo_arr['age'] = age
        elif int(id) == 2:
            sex = request.POST.get("sex")
            myinfo_arr['sex'] = sex
        elif int(id) == 3:
            peoplenum = request.POST.get("peoplenum")
            myinfo_arr['peoplenum'] = peoplenum
        elif int(id) == 4:
            job = request.POST.get("job")
            myinfo_arr['job'] = job
        elif int(id) == 5:
            school = request.POST.get("school")
            major =  request.POST.get("major")
            graduate = school + major
            myinfo_arr['graduate'] = graduate
        elif int(id) == 6:
            mbti = request.POST.get("mbti")
            myinfo_arr['mbti'] = mbti
        elif int(id) == 7:
            army = request.POST.get("army")
            myinfo_arr['army'] = army
        elif int(id) == 8:
            height = request.POST.get("height")
            myinfo_arr['height'] = height
        elif int(id) == 9:
            body = request.POST.get("body")
            myinfo_arr['body'] = body
        elif int(id) == 10:
            eyes = request.POST.get("eyes")
            myinfo_arr['eyes'] = eyes
        elif int(id) == 11:
            face = request.POST.get("face")
            myinfo_arr['face'] = face
        elif int(id) == 12:
            hobby = request.POST.get("hobby")
            myinfo_arr['hobby'] = hobby

        return redirect(f"/my/{index}")
    context = {'count':int(id)}
    return render(request, "myapp/my.html",context)
    
'''
이런 방식을 사용해도 된다
def my(request):
    article = 'my'
    template = loader.get_template(myapp/my.html)
    context = {"article":article}
    return HttpResponse(template.render(context,request))

'''
@csrf_exempt
def you(request):
    article = 'you'
    context = {"article":article}
    return render(request, "myapp/you.html", context)

@csrf_exempt
def choose(request):

    return render(request, "myapp/choose.html")
      
@csrf_exempt
def matching(request):
    article = 'matching'
    context = {"article":article}
    return render(request, "myapp/matching.html", context)
    
@csrf_exempt
def matching2(request):

    return render(request, "myapp/matching2.html")
@csrf_exempt
def matching3(request):

    return render(request, "myapp/matching3.html")
@csrf_exempt
def error(request):

    return render(request, "myapp/error.html")
@csrf_exempt
def result(request):
    article = 'result'
    context = {"article":article}
    return render(request, "myapp/result.html", context)
    
@csrf_exempt
def menu(request):
    article = 'menu'
    context = {"article":article}
    return render(request, "myapp/menu.html", context)
    