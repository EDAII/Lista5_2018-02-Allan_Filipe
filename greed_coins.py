def coin_changing(coins_list, change_value):

    current_position = len(coins_list) - 1
    coins_selected = []

    while change_value != 0:
        if coins_list[current_position] > change_value:
            current_position -= 1
        elif current_position < 0:
            return "não existe solução"
        else:    
            change_value -= coins_list[current_position]
            coins_selected.append(coins_list[current_position])

    return coins_selected


coins_list = [1, 5, 10, 25, 100]
change_value = 289

coins_selected = coin_changing(coins_list, change_value)

print("As moedas selecionadas foram: ", coins_selected)
print("O número de moedas é: ", len(coins_selected))