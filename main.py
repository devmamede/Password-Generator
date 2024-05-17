import random
import string

def generate(qtd_caractere, hasNumber, hasSpecialChar):
    caracteres = {
        (True, True): lambda: string.ascii_letters + string.digits + string.punctuation,
        (True, False): lambda: string.ascii_letters + string.digits,
        (False, True): lambda: string.ascii_letters + string.punctuation,
        (False, False): lambda: string.ascii_letters
    }[(hasNumber, hasSpecialChar)]()
    
    print('password: ', caracteres)
    password = [random.choice(caracteres) for _ in range(qtd_caractere)]
    
    return ''.join(password) 
    

print(generate(10, True, True))


