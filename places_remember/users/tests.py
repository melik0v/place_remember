from django.test import TestCase
from .models import CustomUser


class UsersTestCase(TestCase):
    def test_create_user(self):
        # create test_user
        user_1 = CustomUser(username="test_user_1")
        user_1.save()

        # create test_user
        user_2 = CustomUser(username="test_user_2")
        user_2.save()

        all_users = CustomUser.objects.all()
        self.assertEqual(len(all_users), 2)

        self.assertEqual(all_users[0].pk, user_1.pk)
        self.assertEqual(all_users[1].pk, user_2.pk)
