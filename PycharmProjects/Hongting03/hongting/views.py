from django.shortcuts import render, redirect
from .service import UserProfileService

def create_user_festival(request):
    if request.method == 'POST':
        group_size = request.POST.getlist('group_size')
        profile_data = {
            'group_size': group_size
        }

        user_profile_festival = UserProfileService()
        user_profile_festival.create_user_profile(**profile_data)

        return redirect('home')

    return render(request, '홍대축제.html')
def create_user_profile(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        group_size = request.POST.getlist('group_size')
        extra = request.POST.get('extra')

        # 데이터 가공 또는 검증 부분 추가 가능

        profile_data = {
            'age': age,
            'gender': gender,
            'group_size': group_size,
            'extra': extra
            # 다른 필드 추가 가능
        }

        user_profile_service = UserProfileService()
        user_profile_service.create_user_profile(**profile_data)

        return redirect('home')  # 폼 제출 후 홈 페이지로 이동

    return render(request, 'My.html')  # GET 요청일 때 폼 표시


def home(request):
    return render(request, 'home.html')

def view_user_profiles(request):
    user_profile_service = UserProfileService()
    user_profiles = user_profile_service.get_user_profiles()

    # 조회된 레코드들을 사용하여 작업 수행

    return render(request, 'Result.html', {'user_profiles': user_profiles})
