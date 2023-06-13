def is_palindrome_iterative(word):
    if not word:
        return False

    word = word.lower().replace(" ", "")  # Converter para minúsculas e remover espaços
    length = len(word)

    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            return False

    return True
    raise NotImplementedError
