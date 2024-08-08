import git
import os

import git

def get_differences(repo):
    # Obtener las diferencias entre el commit actual y el commit anterior
    diffs = repo.index.diff(repo.head.commit)
    with open('log.diff', 'w') as f:
        for d in diffs:
            f.write(f"Archivo modificado: {d.a_path}\n")

repo = git.Repo()
get_differences(repo)
