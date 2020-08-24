import setuptools

from cx_Freeze import *


base='Win32GUI' 

includefiles = ['D:\\Scripts\\own projects\\python snake and ladders\\start_page.png','D:\\Scripts\\own projects\\python snake and ladders\\player.png','D:\\Scripts\\own projects\\python snake and ladders\\board.jpg','D:\\Scripts\\own projects\\python snake and ladders\\6.png','D:\\Scripts\\own projects\\python snake and ladders\\5.png', 'D:\\Scripts\\own projects\\python snake and ladders\\4.png','D:\\Scripts\\own projects\\python snake and ladders\\3.png','D:\\Scripts\\own projects\\python snake and ladders\\2.png','D:\\Scripts\\own projects\\python snake and ladders\\1.png']

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Snake And LaddeRs",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]SnakesAndLaddeRs.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     ),
    ("StartMenuShortcut",        # Shortcut
     "StartMenuFolder",          # Directory_
     "Snake And LaddeRs",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]SnakesAndLaddeRs.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}

executables = [Executable("SnakesAndLaddeRs.py", base=base,)]

packages = ["idna", 'time', 'pygame', 'random']
options = {
    'build_exe': {    
        'packages':packages,
        'include_files':includefiles,
        "excludes": ["tkinter", "PyQt4.QtSql", "sqlite3", 
                     "scipy.lib.lapack.flapack",
                     "PyQt4.QtNetwork",
                     "PyQt4.QtScript",
                     "numpy.core._dotblas", 
                     "PyQt5",
                     "matplotlib.tests",
                     "numpy.random._examples",
                     "matplotlib.backends",
                     "pandas",
                     "scipy"]
    },
    "bdist_msi": bdist_msi_options,
}

setup(
    name = "Snakes And LaddeRs",
    options = options,
    version = "1.0",
    description = 'snake and ladders game by Rushi',
    executables = executables
)
