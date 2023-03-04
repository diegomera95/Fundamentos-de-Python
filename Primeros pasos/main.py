userOption = input('Elija piedra, papel o tijera => ')
pcOption = 'papel'

if userOption == pcOption:
    print('Empate!')
elif userOption == 'piedra':
    if pcOption == 'tijera':
        print('piedra gana a tijera')
        print('user gano!')
    else:
        print('papel gana a piedra')
        print('pc gano!')
elif userOption == 'papel':
    if pcOption == 'piedra':
        print('papel gana  piedra')
        print('user gano!')
    else:
        print('tijera gana a papel')
        print('pc gano!')
elif userOption == 'tijera':
    if pcOption == 'papel':
        print('tijera gana  papel')
        print('user gano!')
    else:
        print('piedra gana a tijera')
        print('pc gano!')

