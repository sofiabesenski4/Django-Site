from django.test import TestCase, Client
from django.utils import timezone
from django.test.utils import setup_test_environment
# Create your tests here.
#test cases can test the models and certain aspects of db interactions
#They WILL create a test_db to work with, when instantiating new models etv

from django.urls import reverse

#each one of these classes counts as a test!!!
class SimpleHTTPResponseTests(TestCase):
    def test_index_response_status_bad(self):
        client = Client()
        # this should lead to nothing
        response_bad = client.get("/")
        self.assertEquals(response_bad.status_code, 404)

    def test_index_response_status_good(self):
        client=Client()
        response_good = client.get(reverse("word_count:index"))
        self.assertIs(response_good.status_code,200)
        self.assertContains(response_good, "Word_Count:")


