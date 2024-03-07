import shutil
import os

current_directory = os.path.dirname(__file__)

path_english = os.path.join(current_directory, "inglés", "resume.pdf")
file_english = os.path.join(current_directory, "CV_EN_Raidel_Nápoles.pdf")
path_spanish = os.path.join(current_directory, "español", "resume.pdf")
file_spanish = os.path.join(current_directory, "CV_ES_Raidel_Nápoles.pdf")

shutil.copyfile(path_english, file_english)
shutil.copyfile(path_spanish, file_spanish)
