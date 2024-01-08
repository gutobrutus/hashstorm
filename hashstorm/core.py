import hashlib
import base64

def apply_hash(word, hash_algorithms):
    result = word
    algorithms = hash_algorithms.split(',')
    for algorithm in algorithms:
        if algorithm == 'md5':
            result = hashlib.md5(result.encode('utf-8')).hexdigest()
        elif algorithm == 'base64':
            result = base64.b64encode(result.encode()).decode('utf-8')
        elif algorithm == 'sha1':
            result = hashlib.sha1(result.encode('utf-8')).hexdigest()
        elif algorithm == 'sha256':
            result = hashlib.sha256(result.encode('utf-8')).hexdigest()
        elif algorithm == 'sha512':
            result = hashlib.sha512(result.encode('utf-8')).hexdigest()

    return result

def check_hash(word, hash_target, algorithms):
    return apply_hash(word, algorithms) == hash_target


def process_wordlist(wordlist_file, hash_target, algorithms):
    try:
        with open(wordlist_file, 'r') as wordlist:
            contents = wordlist.read().splitlines()
            for word in contents:
                if check_hash(word, hash_target, algorithms):
                    print(f'O valor em texto claro da hash {hash_target} informada é {word}')
                    return
    except FileNotFoundError as e:
        print(f"Arquivo não encontrado: {e.filename}. Verifique o caminho do arquivo e tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
