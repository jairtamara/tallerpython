import git

def get_differences(repo):
    # Obtener las diferencias entre el commit actual y el commit anterior
    #diff = repo.git.diff('HEAD~1', 'HEAD', '--name-only')Unix
  repo = git.Repo('.')
    
  diffs = repo.index.diff(repo.head.commit)
  for d in diffs:
    print(f"Archivo modificado: {d.a_path}") 
