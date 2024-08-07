from git import Repo

def get_differences():
    # Inicializa el repositorio en el directorio actual
    repo = Repo('.') 
    
    modified_files = repo.git.diff('--name-only', 'HEAD~1', 'HEAD').split('\n')
    
    if modified_files:
        print("Archivos modificados :")
        for mis_diferencias in modified_files:
            print(mis_diferencias)
        contador = len(mis_diferencias)
        print(contador)
    return modified_files

if __name__ == "__main__":
    diferencias = get_differences()    
   

