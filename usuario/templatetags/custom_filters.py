from django import template

register = template.Library()

@register.filter
def length_range(value):
    """
    Retorna un rango de 0 a la longitud del valor (iterable).
    Útil para iterar sobre índices cuando se tienen múltiples listas.
    """
    return range(len(value))

@register.filter
def index(List, i):
    """
    Retorna el elemento en el índice 'i' de una lista.
    """
    try:
        return List[i]
    except IndexError:
        return None # O levanta una excepción, o un valor por defecto