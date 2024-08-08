import git

def get_differences(repo):
    # Obtener las diferencias entre el commit actual y el commit anterior
    diff = repo.git.diff('HEAD~1', 'HEAD', '--name-only')
    for file in diff.splitlines():
        print(f"Archivo modificado: {file}")

repo = git.Repo()
get_differences(repo)
