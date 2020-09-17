#Run from Anaconda shell using the following command:
#python -c "import get_stim_filenames; get_stim_filenames.create_py())"

from os import listdir
from os.path import isfile, join
import csv

def create_py():

	directory = './polls/static/polls/stimuli/'
	filenames = [f for f in listdir(directory) if isfile(join(directory, f))] #limits to filenames only and not subdirectories

	with open('./polls/all_images.py','w') as myFile:
		myFile.write("def get_image_filenames():\n")
		myFile.write("\timage_filenames = [")
		for line in filenames:
			myFile.write('\n\t\t"' + line + '",')

		myFile.write("\n\t]")
		myFile.write("\n\treturn image_filenames")

	print('Task complete.')
	return