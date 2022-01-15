import py_compile
import dis,marshal
import glob
import os
import shutil
from zipfile import PyZipFile, ZIP_STORED
name = "done"
rootname = "monaca"
def compile(url,usetest:bool):
	if usetest == False:
		py_compile.compile(url)
	if usetest == True:
		test()

def test():
		files = glob.glob("scripts//*")
		for file in files:
			#pyc = open("scripts//__pycache__//main.cpython-37.pyc","rb").read()[12:]
				#py_compile.compile(file)
				print(file)
				print('<-test byte->')
			#print(str(pyc))
				if os.path.splitext(file)[1]  == ".py":
					pc = dis.dis(open(file,"r").read())
					py_compile.compile(file,"a")
					#shutil.make_archive(r"C://Users" + "//" + rootname +"//Documents//Electronic Arts//The Sims 4//Mods" + "//_" + name, 'zip', root_dir='scripts//__pycache__//')
					zf = PyZipFile(r"C://Users" + "//" + rootname +"\Documents\Electronic Arts\The Sims 4\Mods//_" + name +".ts4script", mode='w', compression=ZIP_STORED, allowZip64=True, optimize=2)
					zf.writepy(file)
					zf.close()
					#if os.path.exists(r"C://Users" + "//" + rootname +"\Documents\Electronic Arts\The Sims 4\Mods//_" + name +".ts4script"):
					#	os.remove(r"C://Users" + "//" + rootname +"\Documents\Electronic Arts\The Sims 4\Mods//_" + name +".ts4script")
					#os.rename(r"C://Users" + "//" + rootname +"\Documents\Electronic Arts\The Sims 4\Mods//_" + name +".zip",r"C:\Users\monaca\Documents\Electronic Arts\The Sims 4\Mods\_" + name +".ts4script")
				#print(pc)
			#pyc = marshal.loads(pyc)
			#dis.dis(pyc)

print('compiler is launched')
compile("scripts//main.py",True)
