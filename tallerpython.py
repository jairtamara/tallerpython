import git

def get_differences(repo):

  diffs = repo.index.diff(repo.head.commit)
  for d in diffs:
    print(f"Archivo modificado: {d.a_path}") 
