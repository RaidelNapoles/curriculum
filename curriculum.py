import shutil

path_english = r"./inglés/resume.pdf"
file_english = r"./CV_EN_Raidel_Nápoles.pdf"
path_spanish = r"./español/resume.pdf"
file_spanish = r"./CV_ES_Raidel_Nápoles.pdf"

shutil.copyfile(path_english, file_english)
shutil.copyfile(path_spanish, file_spanish)