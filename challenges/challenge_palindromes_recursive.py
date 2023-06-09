def is_palindrome_recursive(word, low_index=0, high_index=None):
    if high_index is None:
        high_index = len(word) - 1

    if low_index >= high_index:
        return True

    if word[low_index].lower() != word[high_index].lower():
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

    raise NotImplementedError
