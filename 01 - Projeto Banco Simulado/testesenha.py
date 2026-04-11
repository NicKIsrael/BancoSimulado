while (True):
    confirmar = ""
    senha = input("Digite sua nova senha(Mínimo de 6 dígitos): ")
    if len(senha) < 6:
        print("Senha muito pequena! Tente novamente!")
    elif not senha.isdigit():
         print("A senha só deve conter números! Tente novamente!")
    else:
        print(f"Senha: {senha}")
        confirmar = input("Confirme sua senha: ")

        while (True):
            if confirmar != senha:
                confirmar = input("Senhas diferentes, confirme novamente: ")
            else:
                print("Senha confirmada!")
                break
    