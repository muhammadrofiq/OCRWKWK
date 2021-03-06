import cv2
import numpy as np
import os

import Preprocess
import KemungkinanPlat
import CharDetect
import getallsub
#import kirim


resultdst = "output/"
resultplat = "output/sgmt-plat"

with open('data/database.txt') as f:
	database=[line.strip() for line in f]



error = 0.8

writeresult = True
showstep= True

SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)


def main(imgdir):
	acc =0
	listPlat = []
	status=0
	Listkombinasideteksi=[]
	masuk=0
	tolak=0


	cv2.destroyAllWindows()
	print "start"
	##################### KNN LOAD MODEL ################################3

	blnKNNTrainingSuccessful = CharDetect.loadKNNDataAndTrainKNN()
	if blnKNNTrainingSuccessful == False:
		print "\nerror: KNN traning was not successful\n"


	#################### load image #####################################
	image = cv2.imread(imgdir)
	imagecopy = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	################### load cascade classifier #########################
	detector = cv2.CascadeClassifier('cscd/plat-80-25stage.xml')
	rects = detector.detectMultiScale(gray, scaleFactor=1.01,minNeighbors=1, minSize=(75, 75))


	################## plate region detection using harr ################
	for (i, (x, y, w, h)) in enumerate(rects):
		cv2.rectangle(imagecopy, (x, y), (x + w, y + h), (0, 0, 255), 2)
		crop_img = image[y:y+(h), x:x+(w)]
		crop_img = 255-crop_img
		Gray, Tresh = Preprocess.preprocess(crop_img)
		PosPlat= KemungkinanPlat.KemungkinanPlat(crop_img,x,y,w,h)
		PosPlat.imgGrayscale = Gray
		PosPlat.imgThresh = Tresh
		listPlat.append(PosPlat)
	################# sort for the true plat ############################
	if len(listPlat)>0:
		listPlat.sort(key = lambda PosPlat: PosPlat.intArea, reverse = True)
		if showstep == True:
			cv2.imshow("true-plat", listPlat[0].imgGrayscale)
			cv2.imshow("original", imagecopy)
			cv2.waitKey(0)
			#print len(listPlat)


		if len(listPlat) > 0:
			TruePlates = CharDetect.detectCharsInPlates(listPlat[0],imgdir)
			lenplat=imgdir.replace("img/","")
			lenplat=lenplat.replace(".jpg","")
			print lenplat
			print TruePlates.strChars
			acc = float(len(TruePlates.strChars))/len(lenplat)
			if acc > 1:
				sub=acc-1
				acc=acc-sub
			'''
			for plat in database:
				if TruePlates.strChars in database:
					status=1
					break
			'''
			#'''
			Listkombinasideteksi=getallsub.get_all_substrings(TruePlates.strChars, error)
			#print Listkombinasideteksi
			for subchar in Listkombinasideteksi:
				for plat in database:
					if subchar in plat:
						status=1

			#'''

			if status == 1 :
				print "silahkan masuk"
				#kirim.sukses()
				masuk=1
			else:
				print "pergisana!"
				#kirim.gagal()
				tolak=1
			if writeresult == True:
				if not os.path.exists(resultplat):
					os.makedirs(resultplat)
				imgdir=imgdir.replace("img","")
				print resultplat+imgdir
				cv2.imwrite(resultplat+imgdir, TruePlates.imgThresh)
	if len(listPlat)==0:
		print("no plate detected")
		#kirim.gagal()
	print "end"



	return acc, masuk , tolak


#########################################################3

if __name__ == "__main__":
    main()
