from solver_limiarizacao_de_imagem import solve_limiarizar_imagem
from utils.buscar_imagem import buscar_imagem

def main():
    print('Escolha uma imagem para realizar a limiarizacao:')
    try:
        imagem_path = buscar_imagem()
        solve_limiarizar_imagem(imagem_path)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
