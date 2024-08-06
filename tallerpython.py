import git

def get_differences(repo):
    # Obtener las diferencias entre el commit actual y el commit anterior
    #diff = repo.git.diff('HEAD~1', 'HEAD', '--name-only')Unix

   MODIFIED=$(git diff --name-only HEAD~ HEAD)
   echo "$MODIFIED"

    # Crear una lista con las diferencias
    differences_list = diff.splitlines()

    return differences_list

# Inicializar el repositorio Git
repo = git.Repo()

# Obtener las diferencias
differences = get_differences(repo)

# Imprimir las diferencias
for difference in differences:
    print(difference)
