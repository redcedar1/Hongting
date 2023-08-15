from django.shortcuts import render

from .models import UserProfile
from .service import UserProfileService

def create_user_profile(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        gender = request.POST.get('sex')
        group_size = request.POST.get('group_size')
        occupation = request.POST.get('occupation')
        school_major = request.POST.get('school_major')
        mbti = request.POST.get('mbti')
        military_service = request.POST.get('military_service')
        height = request.POST.get('height')
        body_type = request.POST.get('body_type')
        double_eyelids = request.POST.get('double_eyelids')
        face_shape = request.POST.get('face_shape')
        interests = request.POST.get('interests')
        self_intro = request.POST.get('self_intro')

        profile_data = {
            'age': age,
            'gender': gender,
            'group_size': group_size,
            'occupation': occupation,
            'school_major': school_major,
            'mbti': mbti,
            'military_service': military_service,
            'height': height,
            'body_type': body_type,
            'double_eyelids': double_eyelids,
            'face_shape': face_shape,
            'interests': interests,
            'self_intro': self_intro,
        }

        user_profile = UserProfileService.create_user_profile(profile_data)
        return render(request, 'home.html', {'user_profile': user_profile})

    return render(request, 'matching.html')


from django.db.models import Q

def match_profiles(selected_category01, selected_value01, selected_category02, selected_value02):
    q1 = Q()
    q2 = Q()

    if selected_category01 == 'mbti':
        q1 |= Q(mbti=selected_value01)
    elif selected_category01 == 'height':
        q1 |= Q(height=float(selected_value01))
    elif selected_category01 == 'age':
        q1 |= Q(age=int(selected_value01))

    # 나머지 필드들에 대한 Q 객체 추가

    if selected_category02 == 'interests':
        q2 |= Q(interests__icontains=selected_value02)
    elif selected_category02 == 'body_type':
        q2 |= Q(body_type=selected_value02)
    elif selected_category02 == 'gender':
        q2 |= Q(gender=selected_value02)
    # 나머지 필드들에 대한 Q 객체 추가

    matches = UserProfile.objects.filter(q1 & q2)
    return matches
