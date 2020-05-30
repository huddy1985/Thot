#!/usr/bin/python3
from distutils.core import setup
import glob

def files(m, p):
	d = os.path.dirname(p)
	

setup(
	name="thot",
	version="0.9",
	description = """Document generator from wiki-like text files.""",
	author = "Hugues Casse",
	author_email = "hug.casse@gmail.com",
	license = "GPLv3",
	packages = ['thot', 'thot/mods', 'thot/backs'],
	scripts = ['bin/thot'],
	data_files = [
		("share/thot/css/minima/", glob.glob("css/minima/*.css")),
		("share/thot/css/minima/", glob.glob("css/minima/*.css"))
	]
)
