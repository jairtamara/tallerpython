import git

def get_changes(repo, file_path):
    commits = repo.git.log('--oneline', '--', file_path).splitlines()
    return commits

repo = git.Repo()
file_path = sys.argv[1]
changes = get_changes(repo, file_path)

print("Cambios en el archivo:", file_path)
for change in changes:
    print(change)
