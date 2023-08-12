from .models import UserProfile

class UserProfileService:
    def create_user_profile(self, age, gender, group_size, extra):
        user_profile = UserProfile(age=age, gender=gender, group_size=group_size, extra=extra)
        user_profile.save()
        return user_profile

    def get_user_profiles(self):
        return UserProfile.objects.all()

    def get_matching_profiles(self, age, gender, group_size):
        matching_profiles = UserProfile.objects.filter(age=age, gender=gender, group_size=group_size)
        return matching_profiles
