def main():
    texto = input()
    convertido = convert(texto)
    print(convertido)

def convert(texto):
    nuevo = texto.replace(':)','🙂')
    nuevo = nuevo.replace(':(','🙁')
    return nuevo

main()