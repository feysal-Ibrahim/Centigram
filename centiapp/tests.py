from django.test import TestCase
from .models import Image , Comment


# Create your tests here.
class ImageTestClass( TestCase ):
    def setUp(self):
        self.image=Image( image='image' , caption='caption' , upload_date='upload_date' , user='feysal',likes='0',profile='profile' )
        self.image.save( )

    def test_instance(self):
        self.assertTrue( isinstance( self.image , Image ) )

    def test_saving_image(self):
        self.image.save_image( )
        images=Image.objects.all( )
        self.assertTrue( len( images )>0 )