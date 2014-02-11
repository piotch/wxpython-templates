import shutil
import fabric.api as f 
from presenters import NAME, VERSION
name = NAME + VERSION
archive_name = name + '.zip'

f.env.hosts = ['pierre3@host.host']

def build_exe():
	f.local('pyinstaller pyinstaller.spec')

def build_doc():
    f = open('doc/source.html')
    doc = f.read().format(NAME=NAME, VERSION=VERSION)
    f.close()
    f = open('doc/index.html', 'w')
    f.write(doc)
    f.close()

def archive():
    shutil.make_archive(
        base_name = name, 
        format = 'zip', 
        root_dir = 'dist')

def upload():
    remote_folder = 'beytiskimu.net/utl/%s/' % NAME
    f.put(archive_name, remote_folder)
    f.put('doc/index.html', remote_folder)

def clean():
    try: f.local('rm doc/index.html')
    except: pass
    try: f.local('rm ' + archive_name)
    except: pass
    try: f.local('rm -rf build/')
    except: pass
    try: f.local('rm -rf dist/')
    except: pass

def build():
    build_exe()
    build_doc()

def publish():
    build()
    archive()
    upload()
    clean()
