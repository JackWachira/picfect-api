from rest_framework.test import APITestCase

from api.models import Image

# Facebook graphapi test user access token
access_token = 'EAAXD3aw3MAgBAIe1S3ZACMLPgEI50E5LZB6TOBxNp3QicHEQtZA4qG79tqqv4rZ\
                AKSecDWh0V8DuWWupgB6h9Dkwwi3W7wqZB4zCauy5L4ivpKAYJgU4epoFNh5CPZAN\
                ZBMlmNf2k2HLViuN9ZAGDdgFvUBvwP2HLisZD'


class ImageAPITest(APITestCase):

    def setUp(self):
        """Create test user and test images"""

        self.client.get("/api/register/facebook/?access_token=" + access_token)
        Image.objects.create(name="adventure.png", original_image="images/adventure.png",
                             date_created="2016-08-03 11:12:12.959349+03",
                             date_modified="2016-08-03 11:12:12.95939+03",
                             category=1, uploader_id=1)
        Image.objects.create(name="fashion.png", original_image="images/fashion.png",
                             date_created="2016-08-03 11:12:12.959349+03",
                             date_modified="2016 - 08 - 03 11: 12: 12.95939 + 03",
                             category=4, uploader_id=1)

    def test_unauthorized_access_is_not_allowed(self):
        """Test that a user cannot access API without credentials."""

        response = self.client.get('/api/images/')
        self.assertEqual(response.status_code, 401)
        detail = response.data.get('detail')
        self.assertIn('Authentication credentials were not provided.', detail)

    def test_get_all_images(self):
        """Test that a GET to /api/images/ returns all images."""

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer facebook ' + access_token)
        response = self.client.get('/api/images/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.data), 2)

    def test_save_edited_image(self):
        """Test that a POST to /api/images/edits/(?P<thumbnail_id>[0-9]+)/ saves edited image."""

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer facebook ' + access_token)
        response = self.client.post('/api/images/edits/1/', {'category': 1})
        self.assertEqual(201, response.status_code)

    def test_get_thumbnails(self):
        """Test that a GET to api/images/(?P<image_id>[0-9]+)/thumbnails/ gets associated thumbnails."""

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer facebook ' + access_token)
        response = self.client.get('/api/images/1/thumbnails/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(len(response.data), 11)

    def test_update_image_category(self):
        """Test that a PUT to api/images/(?P<pk>[0-9]+)/ updates image category."""

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer facebook ' + access_token)
        response = self.client.put(
            '/api/images/1/', {'category': 4})
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.data.get('category'), 4)

    def test_login_successful(self):
        """Test that a GET to api/register/(?P<backend>[^/]+)/ logins user successfully"""

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer facebook ' + access_token)
        response = self.client.get(
            "/api/register/facebook/?access_token=" + access_token)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.data, "Login Successful!")
