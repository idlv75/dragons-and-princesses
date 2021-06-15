------------------------------------------------------------------------------------------------------------------------------------------------------------------------

On machine #1:

Python is presented and properly configured:
root@ip-10-0-0-142:/var/tmp/dragons-and-princesses# which python
/usr/bin/python
root@ip-10-0-0-142:/var/tmp/dragons-and-princesses# which python3
/usr/bin/python3


root@ip-10-0-0-142:/var/tmp/dragons-and-princesses# pyinstaller --onefile Dragons_and_Princesses.py
53 INFO: PyInstaller: 4.3
53 INFO: Python: 3.6.9
54 INFO: Platform: Linux-5.4.0-1045-aws-x86_64-with-Ubuntu-18.04-bionic
54 INFO: wrote /var/tmp/dragons-and-princesses/Dragons_and_Princesses.spec
57 INFO: UPX is not available.
58 INFO: Extending PYTHONPATH with paths
['/var/tmp/dragons-and-princesses', '/var/tmp/dragons-and-princesses']
64 INFO: checking Analysis
64 INFO: Building Analysis because Analysis-00.toc is non existent
64 INFO: Initializing module dependency graph...
66 INFO: Caching module graph hooks...
71 WARNING: Several hooks defined for module 'win32ctypes.core'. Please take care they do not conflict.
73 INFO: Analyzing base_library.zip ...
3042 INFO: Caching module dependency graph...
3183 INFO: running Analysis Analysis-00.toc
3205 INFO: Analyzing /var/tmp/dragons-and-princesses/Dragons_and_Princesses.py
3375 INFO: Processing module hooks...
3375 INFO: Loading module hook 'hook-pickle.py' from '/usr/local/lib/python3.6/dist-packages/PyInstaller/hooks'...
3377 INFO: Loading module hook 'hook-heapq.py' from '/usr/local/lib/python3.6/dist-packages/PyInstaller/hooks'...
3378 INFO: Loading module hook 'hook-difflib.py' from '/usr/local/lib/python3.6/dist-packages/PyInstaller/hooks'...
3379 INFO: Loading module hook 'hook-encodings.py' from '/usr/local/lib/python3.6/dist-packages/PyInstaller/hooks'...
3435 INFO: Loading module hook 'hook-xml.py' from '/usr/local/lib/python3.6/dist-packages/PyInstaller/hooks'...
3670 INFO: Looking for ctypes DLLs
3671 INFO: Analyzing run-time hooks ...
3676 INFO: Looking for dynamic libraries
3823 INFO: Looking for eggs
3824 INFO: Python library not in binary dependencies. Doing additional searching...
3857 INFO: Using Python library /usr/lib/x86_64-linux-gnu/libpython3.6m.so.1.0
3861 INFO: Warnings written to /var/tmp/dragons-and-princesses/build/Dragons_and_Princesses/warn-Dragons_and_Princesses.txt
3883 INFO: Graph cross-reference written to /var/tmp/dragons-and-princesses/build/Dragons_and_Princesses/xref-Dragons_and_Princesses.html
3887 INFO: checking PYZ
3887 INFO: Building PYZ because PYZ-00.toc is non existent
3887 INFO: Building PYZ (ZlibArchive) /var/tmp/dragons-and-princesses/build/Dragons_and_Princesses/PYZ-00.pyz
4222 INFO: Building PYZ (ZlibArchive) /var/tmp/dragons-and-princesses/build/Dragons_and_Princesses/PYZ-00.pyz completed successfully.
4225 INFO: checking PKG
4225 INFO: Building PKG because PKG-00.toc is non existent
4225 INFO: Building PKG (CArchive) PKG-00.pkg
6637 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
6638 INFO: Bootloader /usr/local/lib/python3.6/dist-packages/PyInstaller/bootloader/Linux-64bit/run
6639 INFO: checking EXE
6639 INFO: Building EXE because EXE-00.toc is non existent
6639 INFO: Building EXE from EXE-00.toc
6639 INFO: Appending archive to ELF section in EXE /var/tmp/dragons-and-princesses/dist/Dragons_and_Princesses
6664 INFO: Building EXE from EXE-00.toc completed successfully.
root@ip-10-0-0-142:/var/tmp/dragons-and-princesses# 


Change directoy to "dist" which is the default location for the compiled exe:

root@ip-10-0-0-142:/var/tmp/dragons-and-princesses# cd dist/
root@ip-10-0-0-142:/var/tmp/dragons-and-princesses/dist# ll
total 5768
drwxr-xr-x 2 root root    4096 Jun 15 17:29 ./
drwxr-xr-x 6 root root    4096 Jun 15 17:29 ../
-rwxr-xr-x 1 root root 5896264 Jun 15 17:29 Dragons_and_Princesses*


Copy the input.ymal to this directory:

root@ip-10-0-0-142:/var/tmp/dragons-and-princesses/dist# cp ../input.yaml .
root@ip-10-0-0-142:/var/tmp/dragons-and-princesses/dist# ll
total 5772
drwxr-xr-x 2 root root    4096 Jun 15 17:30 ./
drwxr-xr-x 6 root root    4096 Jun 15 17:29 ../
-rwxr-xr-x 1 root root 5896264 Jun 15 17:29 Dragons_and_Princesses*
-rw-r--r-- 1 root root      69 Jun 15 17:30 input.yaml


Test as NOT root user without sudo:

ubuntu@ip-10-0-0-142:/var/tmp/dragons-and-princesses/dist$ whoami
ubuntu
ubuntu@ip-10-0-0-142:/var/tmp/dragons-and-princesses/dist$ ./Dragons_and_Princesses 
13
2
3 5



------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Testing on another machine where python is broken:

[ec2-user@ip-10-0-0-45 tmp]$ which python
/usr/bin/which: no python in (/home/ec2-user/.local/bin:/home/ec2-user/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin)
[ec2-user@ip-10-0-0-45 tmp]$ which python3
/usr/bin/which: no python3 in (/home/ec2-user/.local/bin:/home/ec2-user/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin)


Make sure we are NOT root:

[ec2-user@ip-10-0-0-45 ~]$ whoami
ec2-user


Cloning the executable file:

[ec2-user@ip-10-0-0-45 tmp]$ git clone https://github.com/acocaori/temp_exe.git
Cloning into 'temp_exe'...
Username for 'https://github.com': acocaori
Password for 'https://acocaori@github.com': 
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 0), reused 4 (delta 0), pack-reused 0
Unpacking objects: 100% (7/7), 5.56 MiB | 16.68 MiB/s, done.


Verify content:

[ec2-user@ip-10-0-0-45 tmp]$ cd temp_exe/
[ec2-user@ip-10-0-0-45 temp_exe]$ ll
total 5768
-rwxrwxr-x. 1 ec2-user ec2-user 5896264 Jun 15 17:22 Dragons_and_Princesses
-rw-rw-r--. 1 ec2-user ec2-user      69 Jun 15 17:22 input.yaml
-rw-rw-r--. 1 ec2-user ec2-user      20 Jun 15 17:22 README.md

Execute seccssfully:

[ec2-user@ip-10-0-0-45 temp_exe]$ ./Dragons_and_Princesses 
13
2
3 5
[ec2-user@ip-10-0-0-45 temp_exe]$ 

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
