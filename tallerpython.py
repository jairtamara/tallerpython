import subprocess

def get_modified_files():
    # Ejecuta el comando git diff y captura la salida
    output = subprocess.check_output(['git', 'diff', '--name-only', 'HEAD~', 'HEAD'])
    # Decodifica la salida a string y elimina el salto de línea al final
    modified_files = output.decode('utf-8').strip()
    return modified_files

if __name__ == '__main__':
    modified_files = get_modified_files()
    print(modified_files)
