import subprocess

def get_modified_files():
    try:
        modified_files = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD~', 'HEAD']).decode('utf-8').splitlines()
    except subprocess.CalledProcessError:
        modified_files = []
    return modified_files

if __name__ == '__main__':
    modified_files = get_modified_files()
    print(modified_files)
