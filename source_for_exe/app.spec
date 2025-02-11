# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['/home/ed/projects/tel/miner_build/pythonObfuscatePyinstall/source_for_exe/armor_hashed/app.py'],
    pathex=[],
    binaries=[],
    datas=[('/home/ed/projects/tel/miner_build/pythonObfuscatePyinstall/source_for_exe/90-Wildlife-1200x834.jpg', './')],
    hiddenimports=['cv2', 'numpy', 'sys', 'signal', 'os'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
