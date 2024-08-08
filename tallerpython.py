import git
import os

def get_differences(log_file='diff_log.lis'):
    # Inicializar el repositorio en la ruta actual
    repo = git.Repo('.')

    # Obtener las diferencias entre el commit actual y el commit anterior
    diffs = repo.index.diff(repo.head.commit)
    
    # Abrir el archivo en modo append y escribir el resumen
    with open(log_file, 'a') as log:
        for d in diffs:
            summary = f"Archivo modificado: {d.a_path}"
            log.write(summary + '\n')  # Escribir el resumen en el archivo .lis

    # Leer el contenido del log
    with open(log_file, 'r') as log:
        log_content = log.read()

    # Escribir el contenido del log en el summary de GitHub Actions usando echo
    summary_file = os.getenv('GITHUB_STEP_SUMMARY')
    if summary_file:
        os.system(f'echo "### Resumen de cambios" >> {summary_file}')
        os.system(f'echo "{log_content}" >> {summary_file}')
    else:
        print("GITHUB_STEP_SUMMARY no está disponible.")

# Ejemplo de uso
get_differences()
