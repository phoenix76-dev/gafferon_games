from django.test import TestCase, Client
from .models import *
from django.contrib.auth.models import User

# Create your tests here.


class TestList(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

        u = User(username='admin', first_name='Glenn', last_name='Fiedler', password='200509Ff')
        u.save()

        t1 = Tag(title='networking')
        t2 = Tag(title='physics')
        t1.save()
        t2.save()

        c1 = Category(title='white papers')
        c1.save()

        a1 = Article(title='article', subtitle='subtitle', author=User.objects.get(username='admin'),
                     category=c1)
        a1.save()
        a1.tags.add(t1, t2)

    def test_author(self):
        response = self.client.get('/')
        print(response.context['articles'][0].author.first_name)
