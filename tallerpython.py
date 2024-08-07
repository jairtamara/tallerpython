from git import Repo

def get_differences():
    # Inicializa el repositorio en el directorio actual
    repo = Repo('.')
    
    # Obtén las diferencias entre el HEAD y el ORIG_HEAD
    #modified_files = repo.git.diff('HEAD', 'FETCH_HEAD', '--name-only')
    modified_files = repo.git.diff('--name-only', 'HEAD~1', 'HEAD').split('\n')    
    return modified_files

if __name__ == "__main__":
    diferencias = get_differences()
    
    if diferencias:
        print("Archivos modificados :")
        for mis_diferencias in diferencias:
            print(mis_diferencias)
    count = len(mis_diferencias)    
    else:
        print("No hay diferencias después del último push.")

