from django.test import TestCase
from rest_framework.test import APIClient

from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title = "Ice Cream",   price =  5.00,  inventory = 100)
        self.menu2 = Menu.objects.create(title = "Pancake",   price =  7.50,  inventory = 75)
        self.valid_data = {
            "title" : "Grapes",
            "price" :  4.00,
            "inventory" : 60
            }
        self.invalid_data = {
            "title" : "",
            "price" :  4.00,
            "inventory" : -100
            }
    
    def test_getall(self):
        # send a GET request
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')
        # get data from db
        menus = Menu.objects.all()
        serializer = MenuSerializer