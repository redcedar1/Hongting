from .models import UserProfile

class UserProfileService:

    def create_user_profile(self, group_size):
        user_profile = UserProfile(group_size=group_size)
        user_profile.save()
        return user_profile

    def get_user_profiles(self):
        return UserProfile.objects.all()

    def get_matching_profiles(self, group_size):
        matching_profiles = UserProfile.objects.filter(group_size=group_size)
        return matching_profiles
