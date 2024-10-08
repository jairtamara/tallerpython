# -*- coding: utf-8 -*-
import git

def get_differences(repo):
    # Obtener las diferencias entre el commit actual y el commit anterior
    diff = repo.git.diff('HEAD~1', 'HEAD', '--name-only' , '--diff-filter=AM')
    with open('log.diff', 'w') as f:
        for file in diff.splitlines():  
            f.write("Archivo modificado: ")
repo = git.Repo(".")
get_differences(repo)
