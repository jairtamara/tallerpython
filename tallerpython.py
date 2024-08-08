import git

def get_differences(log_file='diff_log.lis'):
    # Inicializar el repositorio en la ruta actual
    repo = git.Repo('.')

    # Obtener las diferencias entre el commit actual y el commit anterior
    diffs = repo.index.diff(repo.head.commit)
    
    # Abrir el archivo en modo append y escribir el resumen
    with open(log_file, 'a') as log:
        for d in diffs:
            # Obtener el resumen del diff
            summary = f"Archivo modificado: {d.a_path}"
            print(summary)  # Muestra el resumen en la consola (opcional)
            log.write(summary + '\n')  # Escribir el resumen en el archivo .lis

# Ejemplo de uso
get_differences()
