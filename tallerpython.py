import git

def get_differences(repo):
    # Obtener las diferencias entre el commit actual y el commit anterior
    repo = git.Repo('.')
    diff = repo.git.diff('HEAD~1', 'HEAD', '--name-only')
    for d in diffs:
        print(f"Archivo modificado: {d.a_path}") 
  

    
  #diffs = repo.index.diff(repo.head.commit)
  #for d in diffs:
    #print(f"Archivo modificado: {d.a_path}") 
