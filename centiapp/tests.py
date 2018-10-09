from django.test import TestCase
from .models import Image , Comment , Profile


# Create your tests here.
class ImageTestClass( TestCase ):
    # Set up method
    def setUp(self):
        self.profile=Profile.objects.create( name="profile" )
        self.image=Image( image='image' , caption='caption' , upload_date='upload_date' , user='user',likes='likes',profile=self.profile )

        self.image.save( )

    def save_method(self):
        self.image.save( )
        image=Image.objects.all( )
        self.assertTrue( len( image )>0 )

    # Testing save method
    def save_image(self):
        self.assertEqual( len( Image.objects.all( ) ) , 1 )

    # Tear down method
    def tearDown(self):
        Image.objects.all( ).delete( )

    def delete_image(self):
        Image.delete_image_by_id( self.image.id )
        self.assertEqual( len( Image.objects.all( ) ) , 0 )
