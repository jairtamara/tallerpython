import git

def get_differences(repo,log_file='diff_log.lis'):
    # Obtener las diferencias entre el commit actual y el commit anterior
    #diff = repo.git.diff('HEAD~1', 'HEAD', '--name-only')Unix
  diffs = repo.index.diff(repo.head.commit)
  for d in diffs:
    print(f"Archivo modificado: {d.a_path}")
  log.write(f"Archivo modificado: {d.a_path}\n")
      
