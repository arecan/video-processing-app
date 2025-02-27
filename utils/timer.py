import time

def measure_processing_time(func, *args, **kwargs):
    """
    Mesure le temps d'exécution d'une fonction et retourne le résultat avec le temps en ms.
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    processing_time = (end_time - start_time) * 1000  # Convertir en millisecondes
    return result, processing_time
