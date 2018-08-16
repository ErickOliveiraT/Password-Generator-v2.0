import sys
from cx_Freeze import setup, Executable

setup(
    name = "Password Generator",
    version = "2.0",
    description = "Password Generatorator by Cripto S.a",
    executables = [Executable("gen.py", base = None)])