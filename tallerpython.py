import git

def get_differences(repo):
    # Verificar si el repositorio tiene más de un commit
    if repo.commit_count() > 1:
        # Obtener el commit actual y el commit anterior con fetch_depth=0
        repo.git.fetch(depth=0)
        current_commit = repo.commit('HEAD')
        previous_commit = repo.commit('HEAD~1')

        # Obtener las diferencias entre los dos commits
        differences = current_commit.diff(previous_commit, create_patch=True)

        # Crear una lista con las diferencias
        differences_list = []
        for diff in differences:
            differences_list.append(diff)

        return differences_list
    else:
        print("El repositorio solo tiene un commit, no hay diferencias para mostrar")
        return []

# Inicializar el repositorio Git
repo = git.Repo()

# Obtener las diferencias
differences = get_differences(repo)

# Imprimir las diferencias
for difference in differences:
    print(difference)
