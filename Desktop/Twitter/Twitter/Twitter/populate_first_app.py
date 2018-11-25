import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tweeter_project.settings')
import django
django.setup()
import random
from faker import Faker
from first_app.models import User, Tweet

fakegen =Faker()

#def add_user():
   #user = User.objects.get_or_create(username=user_fake_username, name=user_fake_name, bio=user_fake_bio)[0]
   #user.save()
   #return user

def populate(N=200):
   for entry in range(N):
       user_fake_username = fakegen.user_name()
       user_fake_name = '{} {}'.format(fakegen.first_name(), fakegen.last_name())
       user_fake_bio = fakegen.text()
       user = User.objects.get_or_create(user_name=user_fake_username, name=user_fake_name, bio=user_fake_bio)[0]

       for tweet in range(20):
           record_fake_date = fakegen.date()
           tweet_fake_text = fakegen.text()
           tweet = Tweet.objects.get_or_create(user=user, text=tweet_fake_text, date=record_fake_date)[0]


if __name__ == '__main__':
   print('Starting to populate...')
   populate(20)
   print('Finished populating...')