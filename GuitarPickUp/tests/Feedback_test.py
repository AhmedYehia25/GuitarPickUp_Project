
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import *
import json
class Feedback_test(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        #1 is the id of the supposed feedback
        last_feedback_id = "1"
        full_path = "feedback/" + last_feedback_id
        json_str = "[{}]"
        Feedback.objects.create(feedback = f'feedbacks/{last_feedback_id}' , report = "test",user_id = self.user)
        #create file
        #with open(f'{full_path}','w') as f:
        #    json.dump(json_str,f)
        
        

    def test_feedback(self):
        self.assertEqual(self.user.username ,"testuser")
        feedback1 = Feedback.objects.get(pk = 1)
        self.assertEqual(feedback1.feedback ,"feedbacks/1")


