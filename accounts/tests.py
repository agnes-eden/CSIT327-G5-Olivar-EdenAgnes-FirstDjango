from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AccountFlowTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="student",
            password="SecurePass123!",
            first_name="Sam",
            course="Biology",
        )

    def test_signup_shows_success_message_after_redirect(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newstudent",
                "email": "newstudent@example.com",
                "first_name": "New",
                "last_name": "Student",
                "course": "Chemistry",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("login"))
        self.assertContains(
            response, "Your account has been created. Please log in."
        )

    def test_profile_update_edits_only_authenticated_user(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("profile"),
            {
                "first_name": "Updated",
                "last_name": "Student",
                "email": "student@example.com",
                "course": "Physics",
            },
            follow=True,
        )

        self.user.refresh_from_db()
        self.assertRedirects(response, reverse("profile"))
        self.assertEqual(self.user.first_name, "Updated")
        self.assertEqual(self.user.course, "Physics")
        self.assertContains(response, "Your profile has been updated.")

    def test_profile_requires_authentication(self):
        response = self.client.get(reverse("profile"))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('profile')}",
        )
