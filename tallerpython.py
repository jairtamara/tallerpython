import git

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

    # Leer el contenido del log para agregarlo al summary de GitHub Actions
    with open(log_file, 'r') as log:
        log_content = log.read()

    # Escribir en el summary de GitHub Actions
    with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
        summary.write("### Resumen de cambios\n")
        summary.write(log_content)
        summary.write("\n")

# Ejemplo de uso
get_differences()
