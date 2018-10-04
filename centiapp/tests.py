from django.test import TestCase
from .models import  Image

#Create your tests here.
class ImageTestClass(TestCase):
   def setUp(self):
       self.image=Image( image='image' , caption='caption' , upload_date='upload_date',likes='0' )
       self.image.save( )

   def test_instance(self):
        self.assertTrue( isinstance( self.image , Image ) )

   def test_saving_image(self):
       self.image.save_image( )
       images=Image.objects.all( )
       self.assertTrue( len( images )>0 )

