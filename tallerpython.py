import os
import git

# Clona el repositorio
repo = git.Repo('.')

# Obtiene la lista de archivos modificados o nuevos
modified_files = []
for file in repo.git.diff('--name-only', 'HEAD~', 'HEAD').splitlines():
    modified_files.append(file)

# Obtiene la lista de archivos nuevos
new_files = []
for file in repo.git.ls_files('--others', '--exclude-standard').splitlines():
    new_files.append(file)

# Imprime la lista de archivos modificados o nuevos
print("Archivos modificados:")
for file in modified_files:
    print(file)

print("Archivos nuevos:")
for file in new_files:
    print(file)
