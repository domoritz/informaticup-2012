import sys, os
from glob import glob
from py2exe.build_exe import py2exe
from distutils.core import setup

real_argv = sys.argv

def all_files(path):
	fileLists = dict()
	for root, subFolders, files in os.walk(path):
		for file in files:
			if not root in fileLists:
				fileLists[root] = list()
			fileLists[root].append(os.path.join(root,file))
	print(fileLists)
	return fileLists.items()

if sys.platform == "win32":
	sys.argv = sys.argv[0:1] + [
		"py2exe",
		"--includes", "sip",
		"--dist-dir", "distribution",
		"--compressed",
		"--bundle-files", "3",
		"--optimize", "2",
		"--dll-excludes", "MSVCP90.DLL",
	] + sys.argv[1:]
	setup(
		windows=[{
			"script": "__main__.py",
			"icon_resources": [(1, "icon-draft.ico")],
		}],
		data_files = 
			all_files("dist") +
			all_files("assets") + 
			all_files("documentation") +
			all_files("sample_data")
	)