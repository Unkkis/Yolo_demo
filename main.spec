# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
import sys ; sys.setrecursionlimit(sys.getrecursionlimit() * 5)

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[("test50.mp4", "."), ("logo.ico", "."), ("logo.jpg", "."), ("best.pt", "."), ("yolov8s.pt", "."), ("yolov8n.pt", "."), ("default.yaml", "./ultralytics/yolo/cfg")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='YOLO Demo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='logo.jpg',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
