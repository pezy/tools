import subprocess, re
result = subprocess.run(['svnversion'], stdout=subprocess.PIPE)
version = result.stdout.decode('utf-8')[:4]

subversion = '5,3,3,' + version[1];
print(subversion)
print(version)

file = open("app.rc", "r")
file_regex = re.compile(r"\b(FILEVERSION|FileVersion) \d+,\d+,\d+,\d+\b", re.MULTILINE)
prod_regex = re.compile(r"\b(PRODUCTVERSION|ProductVersion) \d+,\d+,\d+,\d+\b", re.MULTILINE)
ret = re.sub(file_regex, r"\1 " + subversion, str(file.read()))
ret = re.sub(prod_regex, r"\1 " + ",".join(version), ret)

file.close();
file = open("app.rc", "w")
file.write(ret)
file.close();

file = open("svn.hpp", "w")
file.write('#pragma once\n')
file.write('#define VER_PRODUCTVERSION \"' + subversion + '\"\n')
file.write('#define VER_SVN_REVISION ' + version)
