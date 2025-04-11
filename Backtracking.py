import hashlib
import time as t

chars = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
        ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
        ['!', '#', '$', '@']]
length = len(chars)
found = False
password = '0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad'

def permutation(arr, start, end):
    global found
    if start == end:
        if found:
            return
        generate(arr, 0, '')
    else:
        for i in range(start, end):
            if found:
                return
            arr[start], arr[i] = arr[i], arr[start]
            permutation(arr, start + 1, end)
            arr[start], arr[i] = arr[i], arr[start]

def generate(arr, i, thingy):
    global found
    if i < length:
        for c in arr[i]:
            if found:
                return
            generate(arr, i+1, f"{thingy}{c}")
    else:
        if found:
            return
        if hashlib.sha256(thingy.encode()).hexdigest() == password:
            found = True
            print(f"The encrypted password is: {thingy}")

print('Please wait while password is being crakced...')
start_time = t.time()
permutation(chars, 0, len(chars))
print(f"Backtracking took {t.time() - start_time} seconds!\n")
