print('''                        ___
                        |  ~~--.
                        |%=@%%/
                        |o%%%/
                     __ |%%o/
               _,--~~ | |(_/ ._
            ,/'  m%%%%| |o/ /  `\.
           /' m%%o(_)%| |/ /o%%m `\ 
         /' %%@=%o%%%o|   /(_)o%%% `\ 
        /  %o%%%%%=@%%|  /%%o%%@=%%  \ 
       |  (_)%(_)%%o%%| /%%%=@(_)%%%  |
       | %%o%%%%o%%%(_|/%o%%o%%%%o%%% |
       | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
       |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
        \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
         \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
           \_ ~o%=@%(_)%o%%(_)%~ _/
             `\_~~o%%%o%%%%%~~_/'
                `--..____,,--'

''')
print("Bem vindo à sua mais nova avenura.\n Você acorda diante do vazio, voce tem fome!\nTudo que voce dezeja agora é uma pizza!!! ")
escolha = input("voce escolhe 'esperar' ou 'levantar'").lower()
if escolha == "esperar":
    print("voce morre de fome. GAME OVER")
elif escolha == "levantar":
    print("Voce tenta ficar de pé mas como voce tem fome seu ferro esta baixo e voce cai de bunda no chão")
    print("depois de alguns segundos voce se recupera e começa a andar")
    print("Depois do que pareceram horas voce se encontra em um vilarejo no nordeste")
    print("'eles não parecem com quem sabem fazer pizza', pensa voce")
    print("Voce ve uma moça proxima a um estabelecimento  com uma grande placa escrita 'Saloon'")
    escolha = input("Voce pergunta se a moça vende pizza?").lower()
    if escolha == "sim":
        print("Ela sem entender nada puxa um revolver do coldre e aponta pra sua testa")
        print("'quem é vos forasteiro?' pergunta ela")
        print("continua...")
    elif escolha == "nao":
        print("Ela sem entender nada puxa um revolver do coldre e aponta pra sua testa")
        print("'quem é vos forasteiro?' pergunta ela")
        print ("continua...")
    else:
        print("voce tropeça bate a cabeça e morre. GAME OVER")
else:
    print("resposta invalida.GAME OVER")