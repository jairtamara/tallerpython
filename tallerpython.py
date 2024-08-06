from git import Repo

def get_differences():
    # Inicializa el repositorio en el directorio actual
    repo = Repo('.')
    
    # Obtén las diferencias entre el HEAD y el ORIG_HEAD
    #modified_files = repo.git.diff('HEAD', 'FETCH_HEAD', '--name-only')
    modified_files = repo.git.diff('--name-only', 'HEAD','HEAD')  
    return modified_files
