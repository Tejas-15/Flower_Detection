from pickle import NONE
from tensorflow.python.eager.context import context
from PIL import ImageGrab, Image
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import keras.utils as image
import tensorflow as tf
import os
from django.shortcuts import redirect, render
from .models import Info
from .models import Uploaded_Image
from .uploadforms import UploadForm
from django.contrib import messages

#---------------function for calling up our main home page i.e home.html-------------------

def home(request):
	if request.method == 'POST':
		# print("abc", request.FILES.getlist('uploaded_image')[0])
		updb = Uploaded_Image(uploaded_image = request.FILES.getlist('uploaded_image')[0])
		updb.save()
		messages.success( request, (" You have successfully uploaded the image!"))
		return render(request, 'home/home.html')
	else:
		return render(request, 'home/home.html')

#----------------function to upload the user image into the database and to call up upload.html page--------------

def upload(request):
	if request.method =='POST':
		print("hi")
		form = UploadForm(request.FILES)
		if form.is_valid():
			form.save()
	return render(request, 'home/upload.html')



def About(request):
	return render(request, 'home/About.html')

def Help(request):
	return render(request, 'home/Help.html')




def daisy(request):
	return render(request, 'home/daisy.html')

def sunflower(request):
	return render(request, 'home/sunflower.html')

def rose(request):
	return render(request, 'home/rose.html')

def tulip(request):
	return render(request, 'home/tulip.html')

def dandelion(request):
	return render(request, 'home/dandelion.html')

def lotus(request):
	return render(request, 'home/lotus.html')

def Test1(request):

	def predict():
#---------------calling the path of the image that is stored in the databse by the user after uploading it using upload function-----------
		all_image = Uploaded_Image.objects.all()
		# print(all_image)
		for items in all_image:
			variable=items.uploaded_image.path
			# print(variable)
			# type(variable)


		num_classes = 5

		model = tf.keras.Sequential([
		tf.keras.layers.experimental.preprocessing.Rescaling(1./255),
		tf.keras.layers.Conv2D(32, 3, activation='relu'),
		tf.keras.layers.MaxPooling2D(),
		tf.keras.layers.Conv2D(32, 3, activation='relu'),
		tf.keras.layers.MaxPooling2D(),
		tf.keras.layers.Conv2D(32, 3, activation='relu'),
		tf.keras.layers.MaxPooling2D(),
		tf.keras.layers.Flatten(),
		tf.keras.layers.Dense(128, activation='relu'),
		tf.keras.layers.Dense(num_classes)
		])
	
#-------------------calling up the trained model for prediction then using the path of the stored image in database processinf the image to determine flower type -------------
		model = load_model(r"C:\Katalyst\Flower-Detection-WebApp-main\flower_detection\save\flower_api_model.h5")
		validation_image = tf.keras.utils.load_img(os.path.join("C:\Katalyst\Flower-Detection-WebApp-main\media",variable) , target_size=(180,180))
		validation_image = image.img_to_array(validation_image)
		validation_image = np.expand_dims(validation_image,axis=0)
		

		y_predicted = model.predict(validation_image)
		y_predicted[0]

	
		global cn
		global flowername
		global flower1
		cn=np.argmax(y_predicted[0])
		if cn==0 :
			flowername ='Daisy'
			flower1=Info.objects.get(flower_name='Daisy')
		elif cn==1 :
			flowername ='Dandelion'
			flower1=Info.objects.get(flower_name='Dandelion')
		elif cn==2 :
			flowername ='Rose'
			flower1=Info.objects.get(flower_name='Rose')
		elif cn==3 :
			flowername ='Sunflower'
			flower1=Info.objects.get(flower_name='Sunflower')
		elif cn==4 :
			flowername ='Tulip'
			flower1=Info.objects.get(flower_name='Tulip')

		# print(flower1)
	predict()


	context = {	
			"flowername" : flower1,
		}
	return render(request, 'home/test1.html',context)
		