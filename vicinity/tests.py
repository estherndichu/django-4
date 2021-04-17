from django.test import TestCase
from .models import Neighborhood, Profile, Business,Post
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user=User(id=1,username='beau', password='beau1917')
        self.user.save()

        self.hood = Neighborhood(admin=self.user,name='hood',description='all nd msns', location='riruta',health_hotline='0712345678',police_hotline='0723456789',fire_hotline='0789076543')
        self.hood.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def tearDown(self):
        Profile.objects.all().delete() 

class NeighborhoodTestCase(TestCase):
    def setUp(self):
        self.admin = User.objects.create(id=1, username='beau')
        self.hood = Neighborhood.objects.create(id = 1,admin = self.admin,name='Hood',location='Riruta',description='All things serenity',health_hotline='01918171819',police_hotline='0982928292',fire_hotline='0871672736')

    def test_instance(self):
        self.assertTrue(isinstance(self.hood, Neighborhood)) 

    def test_save_hood(self):
        self.hood.save_neighborhood()
        hood = Neighborhood.objects.all()
        self.assertTrue(len(hood) >0)   

class BusinessTestCase(TestCase):
    def setUp(self):
        self.business = Business.objects.create(name='reup',email='g@g.com',address='near bumps',hood='hood')