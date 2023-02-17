
#!/usr/bin/python3

from distutils.core import setup
from distutils.core import Extension

setup(
    name = 'MyModule',
    version = '1.0',
    ext_modules = [Extension('MyModule', ['MyModule.c']), ],
)

# Appel de la première fonction native (example).
print("You start with Python Code")
print(MyModule._IncModuleRefCount())

# Récupération des docstrings des fonctions
print("Doc:", MyModule._IncModuleRefCount().__doc__)
