import sys
import os
sys.path.insert(0, os.getcwd())
from presenters import NAME, VERSION

a = Analysis(['presenters.py'],
             pathex=[os.getcwd()],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='%s%s.exe'%(NAME, VERSION),
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='%s%s'%(NAME, VERSION))
