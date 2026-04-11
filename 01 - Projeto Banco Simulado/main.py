print("Bem-vindo ao Banco Central!")

contas = {}

#Função Criar Conta
def criar_conta():
            while (True):
                #NOME
                #Guardando o nome em uma variável e verificando se são apenas letras utilizando o .isalpha
                nome = input("Digite seu nome completo(Apenas Letras): ")

                if nome.replace(" ", "").isalpha():
                     print(f"Nome registrado! Bem-vindo {nome}!")
                     break
                else:
                     print("Só aceitamos letras! Tente novamente!")

            #DATA DE NASCIMENTO
            while (True):
                datanas = (input("Digite sua data de nascimento(8 dígitos xx/xx/xxxx ): "))
                if len(datanas) != 8:
                    print("Erro! A data de Nascimento deve ter 8 dígitos! (xx/xx/xxxx)")
                elif not datanas.isdigit():
                     print("Erro! Só aceitamos números!")
                else:
                    data_formatada = f"{datanas[:2]}/{datanas[2:4]}/{datanas[4:8]}"
                    print(f"Data de Nascimento registrada! {data_formatada}")
                    break
            
            #CPF
            while (True):
                CPF = input("Digite seu CPF(Apenas números): ")
                if len(CPF) != 11:
                    print("Erro! O CPF precisa ter 11 dígitos!")
                #O .isdigit aqui faz a verificação se realmente são dígitos, aqui não é necessário colocar o len
                #Isso porque o len não reconhece números, então após verificar o len logo acima aqui é apenas verificar se tudo é dígito
                elif not CPF.isdigit():
                    print("Erro! Só aceitamos números!")
                else:
                #Aqui eu utilizo uma espécie de macete para fazer a formatação do CPF
                    cpf_formatado = f"{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}"
                    print(f"CPF Registrado! {cpf_formatado}")
                    break
        
            #SENHA
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

                    while confirmar != senha:
                        confirmar = input("Senhas diferentes! Digite novamente: ")
                        
                    print("Senha confirmada!")
                    break
                        
                    
                    
            return {
                "nome": nome,
                "data_nascimento": data_formatada,
                "cpf": cpf_formatado,
                "senha": senha,
                "saldo": 0.0  # já inicia com saldo zerado
            }               

while True:
    print("Selecione a opção que mais se encaixe com sua vontade: ")

    print("01 - Criar Conta")
    print("02 - Depositar")
    print("03 - Sacar")
    print("04 - Ver saldo")


    opcao = int(input("Digite a opção(01 a 04): "))
    if opcao == 1:
        dados = criar_conta() #Guarda a criação da conta dentro da variável dados
        contas[dados["cpf"]] = dados #Aqui ele chama o Dicionário criado >contas< pega os dados e utiliza >cpf< como chave para buscar contas
        print(f"Conta criada para {dados["nome"]}!") #Aqui ele pesquisa dentro de >dados< o nome 
    
        
    break


        
