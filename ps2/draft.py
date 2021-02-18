def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    secret_word = list(secret_word)
    count = 0
    for i in secret_word:
      if i in letters_guessed:
        count += 1
    if count == len(secret_word):
        return True
    else:
        return False

secret_word = 'barak'
letters_guessed = list('sdkrbsd')

print(is_word_guessed(secret_word, letters_guessed))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = ''
    secret_word = list(secret_word)
    for c in secret_word:
      if c in letters_guessed:
        result = result + c
      else:
        result = result + '_ '
    return result
    # secret_word = 'apple'
    # letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
    # print(get_guessed_word(secret_word, letters_guessed)) '_ pp_ e'

print(get_guessed_word(secret_word, letters_guessed))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string
    result = list(string.ascii_lowercase)
    for i in letters_guessed:
        if i in result:
            result.remove(i)
    return str(result)

letters_guessed = 'abcdya'
print(get_available_letters(letters_guessed))
