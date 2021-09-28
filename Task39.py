#!/usr/bin/python3
import cgi
import subprocess

print("content-type:text/html")
print()

fs=cgi.FieldStorage()
cmd =fs.getvalue('x')
o=subprocess.getoutput("sudo "+cmd)
print(o)
