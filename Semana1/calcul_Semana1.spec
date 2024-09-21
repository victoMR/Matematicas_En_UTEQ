# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['calcul_Semana1.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/raton/OneDrive/Documentos/univ vks/7to Cuatri/Matematicas/venv/Lib/site-packages/customtkinter/__init__.py', 'customtkinter')],
    hiddenimports=[],
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
    a.binaries,
    a.datas,
    [],
    name='calcul_Semana1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
