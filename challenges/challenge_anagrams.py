# Função de ordenação (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# Função auxiliar para mesclar duas metades ordenadas
def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def is_anagram(first_string, second_string):
    # Converter as strings para minúsculas
    first_string = first_string.lower()
    second_string = second_string.lower()

    # Verificar se as palavras passadas no parâmetro são vazias
    if (first_string == "" and second_string == ""):
        return (first_string, second_string, False)

    # Converter as strings para listas de caracteres
    first_list = list(first_string)
    second_list = list(second_string)

    # Ordenar as listas utilizando o algoritmo Merge Sort
    sorted_first_list = merge_sort(first_list)
    sorted_second_list = merge_sort(second_list)

    # Converter as listas ordenadas de volta para strings
    sorted_first_string = "".join(sorted_first_list)
    sorted_second_string = "".join(sorted_second_list)

    # Verificar se as strings ordenadas são iguais
    return (
        sorted_first_string,
        sorted_second_string,
        sorted_first_string == sorted_second_string
    )

    raise NotImplementedError
