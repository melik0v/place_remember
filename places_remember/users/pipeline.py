from social_django.models import UserSocialAuth
import requests


def get_avatar(backend, response, user=None, *args, **kwargs):

    # Get avatar from VK
    if backend.name == "vk-oauth2":
        user_social_auth = (
            UserSocialAuth.get_social_auth_for_user(user.id).get().extra_data
        )
        response = requests.get(
            "https://api.vk.com/method/users.get?user_ids={0}&fields=photo&access_token={1}&v=5.131".format(
                user_social_auth.get("id"), user_social_auth.get("access_token")
            )
        )

        if response.json():
            user.avatar = response.json()["response"][0]["photo"]

    # Get avatar from Google
    if backend.name == "google-oauth2":
        user_social_auth = (
            UserSocialAuth.get_social_auth_for_user(user.id).get().extra_data
        )
        response = requests.get(
            "https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={0}".format(
                user_social_auth.get("access_token")
            )
        )

        if response.json():
            user.avatar = response.json()["picture"]

    user.save()
