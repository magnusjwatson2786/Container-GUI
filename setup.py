import os, sys
from cx_Freeze import setup, Executable

setup(
    name = "Sample Window",
    version = "1.0",
    description = "Container for future .py apps",
    author = "Arun prabhakar",
    options = {'build_exe' : {'include_files' : ['terminal.ico','themes/']}},
    executables = [Executable(
    script="xt.py",
    base="Win32GUI",
    icon="terminal.ico")
    ] 
)