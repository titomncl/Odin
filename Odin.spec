# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['odin/main.py'],
             pathex=['E:\\DEV\\Odin'],
             binaries=[],
             datas=[('odin/config/software_config.yaml', 'config'), ('odin/resources/icons/*', 'resources/icons'),
('odin/resources/trees/*yaml', 'odin/resources/trees'), ('odin/softwareList/*', 'softwareList'), ('venv/', 'venv')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Odin',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='odin\\resources\\icons\\odin.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Odin')
