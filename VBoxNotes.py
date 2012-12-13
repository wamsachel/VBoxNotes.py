#!/usr/bin/env python

#Nice, simple XML parsing walkthrough found at 
#http://www.travisglines.com/web-coding/python-xml-parser-tutorial
#I ended up not using XML parsing at all...

import sys
import argparse
from vboxapi import VirtualBoxManager

def getVMSettingsFilePath (vm_name):
	"""Takes, as an argument: string, the VM name or VM uuid that will be looked up
		Returns: string, the VM's SettingFilePath
	"""
	settings_path = ''
	mgr = VirtualBoxManager(None, None)
	vbox = mgr.vbox
	try:
		machine = vbox.findMachine(vm_name)
	except:
		print ("Error!  VBox does not recognize '%s' as a Virtual Machine" % vm_name)
		exit(1)
	else:
		settings_path = machine.settingsFilePath		
	return settings_path

def getFileHandle(file_name):
	"""Takes, as arguments, the file_name to be opened
		Returns, the file_handle of the opened file
	"""
	try:
		file_handle = open(file_name, 'r+')
	except IOError as e:
		print ("Could not open %s, maybe it does not exist yet.\nAttempting file creation" % file_name)
		try:
			file_handle = open(file_name, 'w')
			file_handle.close()
			file_handle = open(file_name, 'r+')
		except:
			print ("Error!  Could not open %s" % file_name)
			exit(1)
	except:
		print ("Error! Unexpected error thrown when attempting to open %s" % file_name)
		exit(1)
		
	return file_handle
	

def getWriteContents(file_name):
	"""Takes, as arguments, the filename to be read in, if filename==None, then record user input from STDIN
		Returns, string, either contents from filename or STDIN

	"""
	contents = ''
	if (file_name != None):
		try:
			in_file_handle = open(file_name, 'r')
			line = in_file_handle.readline()
			while (line != ''):
				contents += line
				line = in_file_handle.readline()
			print ("\n\n%d lines were read from %s." %(len(contents.splitlines()), file_name))
		except:
			print ("Error!  Exception thrown when attempting to read %s" % file_name)
			exit(1)
	else:
		print ("Enter any notes would like saved with this Virtual Machine\n(press Ctrl-C when done):")
		while (True):
			try:
				contents += raw_input(":") + '\n'
			except KeyboardInterrupt: break
			except EOFError: break
    
	if ((contents != '') and (file_name != None)):
		#A '\n' as already been appened to contents read in from
		#STDIN, however the contents read in from file_name
		#do not have the '\n'
		contents += '\n'
	return contents

def getReadContents(file_handle):
	"""Takes as argument(s): a file_handle
		Returns: string list, containing all the lines read from file_handle		
	"""
	contents=''
	try:
		file_handle.seek(0)
	except: 
		print ("Error!  Exception thrown when attempting file_handle.seek(0)")
		exit(1)
	else:
		try:
			contents = file_handle.readlines()
		except:
			print ("Error!  Exception thrown when attempting to read file contents")
			exit(1)
	return contents

def writeFileContents(file_handle, contents):
		"""Takes as arguments(s): a file_handle that will be written to
									a string containing the text that will be written to the file
			Returns Nothing
		"""
		try:
			file_handle.seek(0,2) #Sets the file_handle position to the end of the line
		except: 
			print ("Error!  Exception thrown when attempting file_handle.seek(0,2)")
			exit(1)
		else:
			try:
				file_handle.write(contents)
			except:
				print ("Error!  Exception thrown when attempting to write file contents")
				exit(1)
			else:
				try:
					file_handle.flush()
				except:
					print("Error!  Exception throw when attempting to flush file_handle")
					exit(1)
		
	
def main((arg_vm_name, arg_filename, arg_write, arg_quiet)):
	
	vm_note_file = getVMSettingsFilePath(arg_vm_name)
	vm_note_file += "-notes.txt" 
	
	file_handle = getFileHandle(vm_note_file)
	
	if (not arg_quiet):
		#No quiet option, so print what has already been previously stored.
		print ("".join(getReadContents(file_handle)))
	
	if (arg_write):
		write_contents = getWriteContents(arg_filename)
		writeFileContents(file_handle, write_contents)
		print ("\n\n%d lines written to %s." %(len(write_contents.splitlines()), vm_note_file))
	
if (__name__=='__main__'):
	#Handle Arguments
	arg_parser = argparse.ArgumentParser()
	
	arg_parser.add_argument('vm_name', help="Either the name of the VM, or its uuid")
	arg_parser.add_argument('-f', '--filename', help="Use the contents of a file for the description value")
	arg_parser.add_argument('-q', '--quiet', action='store_true', help="Tells VBoxNotes to suppress printing out VM Notes")
	arg_parser.add_argument('-w', '--write', action='store_true', help="Write new VM Notes")
	args = arg_parser.parse_args()
 	
	main((args.vm_name, args.filename, args.write, args.quiet))
	
