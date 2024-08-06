from git import Repo

def get_differences():
    # Inicializa el repositorio en el directorio actual
    repo = Repo('.')
    
    # Obtén las diferencias entre el HEAD y el ORIG_HEAD
    modified_files = repo.git.diff('ORIG_HEAD', 'HEAD')
    
    return modified_files

if __name__ == "__main__":
    diferencias = get_differences()
    
    if diferencias:
        print("Archivos modificados después del último push:")
        print(diferencias)
    else:
        print("No hay diferencias después del último push.")
