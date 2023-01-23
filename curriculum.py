import shutil

path_english = r"/home/raidel/Documentos/curriculum/latex/inglés/resume.pdf"
file_english = r"/home/raidel/Documentos/curriculum/latex/CV_EN_Raidel_Nápoles.pdf"
path_spanish = r"/home/raidel/Documentos/curriculum/latex/español/resume.pdf"
file_spanish = r"/home/raidel/Documentos/curriculum/latex/CV_ES_Raidel_Nápoles.pdf"

shutil.copyfile(path_english, file_english)
shutil.copyfile(path_spanish, file_spanish)
