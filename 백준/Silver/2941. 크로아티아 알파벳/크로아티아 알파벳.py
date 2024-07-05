import sys

def count_croatian_alphabet(word):
    croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    count = 0
    i = 0
    while i < len(word):
        if i <= len(word) - 2 and word[i:i+2] in croatian_alphabets:
            count += 1
            i += 2
        elif i <= len(word) - 3 and word[i:i+3] == 'dz=':
            count += 1
            i += 3
        else:
            count += 1
            i += 1
    return count

input_word = sys.stdin.readline().strip()
print(count_croatian_alphabet(input_word))
