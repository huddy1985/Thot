#!/usr/bin/python
import imp
import doc
import os
import parser
import locale
import sys
import optparse
import datetime

# Error handling
def onError(text):
	print ("ERROR:" + text + "\n")
	sys.exit(1)

# Prepare environment
env = { } # os.environ.copy()
env["THOT_VERSION"] = "0.1"
env["THOT_ENCODING"] = locale.getpreferredencoding()
env["THOT_USE_PATH"] = os.getcwd() + "/mods/"
env["THOT_DATE"] = str(datetime.datetime.today())

# Parse argument
oparser = optparse.OptionParser()
oparser.add_option("-t", "--type", action="store", dest="out_type",
	default="xml", help="output type (xml, html, latex, ...)")
oparser.add_option("-o", "--out", action="store", dest="out_path",
	help="output path")
(options, args) = oparser.parse_args()
env["THOT_OUT_TYPE"] = options.out_type
if not options.out_path:
	env["THOT_OUT_PATH"] = ""
else:
	env["THOT_OUT_PATH"] = options.out_path
if args == []:
	input = sys.__stdin__
	env["THOT_FILE"] = "<stdin>"
else:
	input = file(args[0])
	env["THOT_FILE"] = args[0]

# Parse the file
document = doc.Document(env)
handler = parser.Handler(document)
handler.parse(input)
document.dump()

# Output the result
#out_name = env["THOT_OUT_TYPE"]
#out_driver = imp.load_source(out_name, document.env["THOT_OUTS_PATH"] + "/" + out_name + ".py")
#out_driver.DRIVER.output(document)
