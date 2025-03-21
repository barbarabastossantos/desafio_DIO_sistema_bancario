saldo=0
extrato=""
deposito=0
saque=0
LIMITE_SAQUE =500
SAQUE_DIARIO=3
saque_realizado=0



while True: #criei um loop infinito com o True na minha estrutura de repetição while
 #pra obrigar meu usuario a so conseguir sair depois de escolher a opção 5 que vai ter o break
 menu=int(input(
    """
    =============================================================
    ================== MENU =====================================
    =============================================================

    Escolha dentre as opções a operação desejada :

     [1] Saldo
     [2] Deposito
     [3] Saque
     [4] Extrato
     [5] Sair

 => """
 ))

 if menu ==1:
    print(f"Seu saldo atual é de {saldo}")
 elif menu ==2:
      deposito=float(input(" Qula o valor do deposito ?  "))
      if deposito <= 0:
       print("Falha ao depositar! Por favor tente novamente. ")
      else:
        saldo+=deposito
        extrato+= f" Deposito : R$ {deposito:.2f}\n"
        print(f" Deposito de R$ {deposito:.2f} realizado com sucesso") 
 elif menu ==3:
    saque=float(input(" Deseja sacar quanto R$ : "))
    if saque > saldo:
      print(f" Transação não aceita! Saldo insuficiente R$ {saldo:.2f}")
    elif saque > LIMITE_SAQUE:
      print(f"Transação não aceita! permitido saque de R$ {LIMITE_SAQUE:.2F} por vez. ")
    elif saque_realizado >= SAQUE_DIARIO:
      print(" Transação não aceita! Limite de de saque diario já foi atingido. ")
    else:
      extrato+= f"Saque : R$ {saque:.2f}\n"
      saldo-=saque
      saque_realizado+=1
      print(f" Saque de R$ {saque:.2f} realizado com sucesso.")
 elif menu == 4:
   print(
    f"""
       EXTRATO

       
    {extrato}

    Saldo atual R$ {saldo:.2f}

     

   """
   )
 elif menu==5:
   print(
     """
     
     Obrigado por fazer parte da nossa família!
       No Banco Bastos, você é nossa prioridade.
   Estamos sempre à disposição para te ajudar. Até a próxima!
   
          Saindo...  """)
   break 
 else:
   print("Opção invalida! Escolha dentre as opções validas de 1 a 5")
    #eu quero que meu usuario so tenha essas opções , caso ele insita em digitar outro 
    # numero da opção invalida, ai criei esse else
 

#              COMENTANDO O CODIGO


# Fora do loop eu fiz as atribuições das minhas variaveis 
# Minhas variaveis foram : saldo,deposito,saque,
#  extrato (que armazenar tanto o saques como os depositos) eu inicio ela com string vazia
# saldo_realizado ( meu contador , meu usuario so pode fazer 3 saques diarios  essa variavel começa com 0 e vai ate 3)
# no python não exite constante uma palavra reservada como em outras linguagens 
# mas por convenção quando eu quero que não mudem o valor da minha variavel quero uma constante 
# eu sinalizo para os demais programadores usando letras maiusculas
# nesse codigo usei duas que foi LIMITE_SAQUE  QUE SO PODIA SER DE 500 reias  por saque
#e SAQUE_DIARIO que so podia ser feito saque 3 vezes por dia são valores que eu não quero que mude
# o loop e o break eu ja comentei no codigo
# usei multilinhas  de string """" para facilitar meu codigo
# usei tambem  f-string f" e atribuição com operador += -= pra me ajudar no extrato principalmente
#

   
    
