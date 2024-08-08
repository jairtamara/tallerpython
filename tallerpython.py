import git
import os

def get_differences(repo):
    # Correcta indentación
    diff = repo.git.diff('HEAD~1', 'HEAD', '--name-only')
    with open('log.diff', 'w') as f:
        # Correcta indentación
        for d in diffs:
            # Correcta indentación
            f.write(f"Archivo modificado: {d.a_path}\n")

# Correcta indentación
repo = git.Repo()
get_differences(repo)
