from django.shortcuts import render
import time

# Coins list used in coin changing greed algorithm
coins_list = [1, 5, 10, 25, 50, 100]


def home(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.POST['selectedOption']:
        myfile = request.FILES['myfile']
        byte_str = myfile.file.read()

        # Convert to a "unicode" object
        text_obj = byte_str.decode('UTF-8')

        # Choosing algorithm options
        if request.POST['selectedOption'] == "Greed - Coin Changing":
            change_list = read_csv_coin(text_obj.splitlines())
            change_list_results, change_list_times = calculate_all_changes(change_list)
            change_list_full = coin_changing_formating_result(change_list, change_list_results, change_list_times)

            return render(request, 'result.html', {'algorithm': request.POST['selectedOption'],
                                                   'change_list_full': change_list_full,
                                                   'change_list': change_list,
                                                   'change_list_results': change_list_results,
                                                   'change_list_times': change_list_times})

        elif request.POST['selectedOption'] == "Greed - Interval Scheduling":
            columns_descriptions, all_data = read_csv(text_obj.splitlines())

            return render(request, 'result.html', {'columns_descriptions': columns_descriptions})
        else:
            # Nothing to do
            pass
    else:
        # Nothing to do
        pass

    return render(request, 'home.html')


def read_csv_coin(file):
    change_list = []

    for line in file:
        change_list.append(int(line))

    return change_list


def calculate_all_changes(change_list):
    change_list_results = []
    change_list_times = []

    for change in change_list:
        time_initial = time.time()

        change_list_results.append(coin_changing(change))

        time_final = time.time() - time_initial

        change_list_times.append(time_final)

    return change_list_results, change_list_times


def coin_changing(change_value):

    current_position = len(coins_list) - 1
    coins_selected = []

    while change_value != 0:
        if coins_list[current_position] > change_value:
            current_position -= 1
        elif current_position < 0:
            coins_selected.append(-1)
            return coins_selected
        else:
            change_value -= coins_list[current_position]
            coins_selected.append(coins_list[current_position])

    return coins_selected


def coin_changing_formating_result(change_list, change_list_results, change_list_times):
    change_list_full = []

    for i in range(len(change_list)):
        current_vector = []
        current_vector.append("{0:.2f}".format(change_list[i] / 100.00))
        current_vector = add_coins_count(current_vector, change_list_results[i])
        current_vector.append(round(change_list_times[i], 15))
        change_list_full.append(current_vector)

    return change_list_full


def add_coins_count(current_vector, change_list_results):
    coin_1 = 0
    coin_5 = 0
    coin_10 = 0
    coin_25 = 0
    coin_50 = 0
    coin_100 = 0

    for coin in change_list_results:
        if coin == 1:
            coin_1 += 1
        elif coin == 5:
            coin_5 += 1
        elif coin == 10:
            coin_10 += 1
        elif coin == 25:
            coin_25 += 1
        elif coin == 50:
            coin_50 += 1
        elif coin == 100:
            coin_100 += 1
        else:
            # Nothing to do.
            pass

    current_vector.append(coin_1)
    current_vector.append(coin_5)
    current_vector.append(coin_10)
    current_vector.append(coin_25)
    current_vector.append(coin_50)
    current_vector.append(coin_100)

    return current_vector


def read_csv(file):
    all_data = []
    columns_descriptions = []

    # Save all csv data in a list of lists, removing '\n' at the last line element.
    for line in file:
        if not columns_descriptions:
            columns_descriptions = line.split(",")
            columns_descriptions[-1] = columns_descriptions[-1].strip("\n")
        else:
            line_splitted = line.split(",")
            line_splitted[-1] = line_splitted[-1].strip("\n")
            all_data.append(line_splitted)

    return columns_descriptions, all_data
