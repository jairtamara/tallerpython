import git

def get_differences(repo): 
    repo = Repo('.')
    modified_files = repo.git.diff('HEAD~1')
    print(modified_files)
  

    
  #diffs = repo.index.diff(repo.head.commit)
  #for d in diffs:
    #print(f"Archivo modificado: {d.a_path}") 
